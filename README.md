# genpark-local-agent-hardware-access-governor-skill

![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green) ![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple) ![GenPark AI](https://img.shields.io/badge/GenPark-AI--Agent--Skill-orange)

> **GenPark AI Agent Skill** -- Local hardware AI agent access governor enforcing scoped filesystem, permissions and quotas (Plow Latch style)

## Quick Start
```python
python example_usage.py
```

## Architecture
```mermaid
graph LR
  User([User / AI Agent]) -->|JSON Request| Skill[GenPark AI Skill]
  Skill --> CoreEngine[Core Engine]
  CoreEngine -->|Structured Output| User
```

## MCP
```bash
python mcp_server.py
```
