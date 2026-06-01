#!/usr/bin/env python3
"""
MCP Memory Server — persistent key/value memory accessible to any MCP client.
Memories are stored in ~/.mcp-memory/memories.json.
"""

import asyncio
import json
import os
from datetime import datetime, timezone
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

MEMORY_FILE = os.path.expanduser("~/.mcp-memory/memories.json")

app = Server("memory")


def _load() -> dict:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE) as f:
            return json.load(f)
    return {}


def _save(memories: dict) -> None:
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=2)


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="remember",
            description=(
                "Store a piece of information in persistent memory. "
                "Use a short, descriptive key (e.g. 'preferred_language', 'project_stack'). "
                "Overwrites any existing entry with the same key."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "Unique identifier for this memory",
                    },
                    "content": {
                        "type": "string",
                        "description": "The information to store",
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional tags for grouping / filtering",
                    },
                },
                "required": ["key", "content"],
            },
        ),
        Tool(
            name="recall",
            description=(
                "Search stored memories. Returns all entries whose key, content, "
                "or tags contain the query string (case-insensitive). "
                "Pass an empty string to return everything."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term; empty string returns all memories",
                    }
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="list_memories",
            description="List all stored memory keys, optionally filtered by tag.",
            inputSchema={
                "type": "object",
                "properties": {
                    "tag": {
                        "type": "string",
                        "description": "Filter by this tag; omit to list all",
                    }
                },
            },
        ),
        Tool(
            name="forget",
            description="Delete a memory by its exact key.",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Key to delete"}
                },
                "required": ["key"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    memories = _load()

    if name == "remember":
        key = arguments["key"]
        memories[key] = {
            "content": arguments["content"],
            "tags": arguments.get("tags", []),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        _save(memories)
        return [TextContent(type="text", text=f"Stored memory: '{key}'")]

    if name == "recall":
        query = arguments["query"].lower()
        results = {}
        for key, entry in memories.items():
            haystack = " ".join(
                [key, entry["content"]] + entry.get("tags", [])
            ).lower()
            if not query or query in haystack:
                results[key] = entry
        if not results:
            return [TextContent(type="text", text="No memories found.")]
        lines = []
        for key, entry in results.items():
            tags = f"  tags: {', '.join(entry['tags'])}" if entry.get("tags") else ""
            lines.append(f"[{key}]\n{entry['content']}{tags}")
        return [TextContent(type="text", text="\n\n".join(lines))]

    if name == "list_memories":
        tag = arguments.get("tag", "").lower()
        keys = [
            k
            for k, v in memories.items()
            if not tag or tag in [t.lower() for t in v.get("tags", [])]
        ]
        if not keys:
            return [TextContent(type="text", text="No memories found.")]
        return [TextContent(type="text", text="\n".join(f"• {k}" for k in keys))]

    if name == "forget":
        key = arguments["key"]
        if key in memories:
            del memories[key]
            _save(memories)
            return [TextContent(type="text", text=f"Deleted memory: '{key}'")]
        return [TextContent(type="text", text=f"No memory found with key '{key}'")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
