# aegis-target-01 · users service

Small Flask service that serves user profiles from SQLite.

Monitored by [AEGIS](https://github.com/vincivv): every push to this repo is scanned autonomously by an AEGIS sentinel agent.

## Run

```bash
pip install -r requirements.txt && python seed.py && python app.py
```

## Routes

- `GET /health`
- `GET /users/<id>`

## Ops assistant

`agent_tools.py` is an MCP server (`python agent_tools.py`) exposing `run_diagnostic` and `explain_db_error` to the support bot.
