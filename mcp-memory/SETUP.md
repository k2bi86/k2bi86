# MCP Memory Server

Persistent memory for any MCP-compatible AI (Claude Code, Cursor, Claude Desktop, custom agents).  
Memories live in `~/.mcp-memory/memories.json` — one file, every tool reads the same store.

## Tools

| Tool | What it does |
|------|-------------|
| `remember(key, content, tags?)` | Store or update a memory |
| `recall(query)` | Search memories by keyword; empty string returns all |
| `list_memories(tag?)` | List keys, optionally filtered by tag |
| `forget(key)` | Delete a memory |

## Install

```bash
pip install mcp
```

Or with a virtual environment:

```bash
cd mcp-memory
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Wire it up

### Claude Code (`~/.claude/settings.json`)

```json
{
  "mcpServers": {
    "memory": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-memory/server.py"]
    }
  }
}
```

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "memory": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-memory/server.py"]
    }
  }
}
```

### Cursor (`.cursor/mcp.json` in your project or `~/.cursor/mcp.json` globally)

```json
{
  "mcpServers": {
    "memory": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-memory/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/mcp-memory/server.py` with the real path on your machine.  
Use the venv python path if you installed in a virtualenv:  
`/absolute/path/to/mcp-memory/.venv/bin/python`

## Usage examples

```
remember(key="preferred_language", content="Python")
remember(key="current_project", content="Building a RAG pipeline with LangChain", tags=["work", "ai"])
recall(query="ai")
list_memories(tag="work")
forget(key="current_project")
```

## How it works

- Memories are stored as JSON at `~/.mcp-memory/memories.json`
- Any AI client with this MCP server configured reads the same file
- `recall` does case-insensitive substring search across key + content + tags
- No external services, no API keys, no vector DB required
