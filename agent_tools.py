"""Ops assistant: an MCP server that lets the support bot inspect the host and answer questions about the DB."""
import os
import subprocess

from mcp.server.fastmcp import FastMCP
from openai import OpenAI

mcp = FastMCP("ops-assistant")
client = OpenAI()


@mcp.tool()
def run_diagnostic(command: str) -> str:
    """Run a diagnostic command on the app host (e.g. 'df -h', 'uptime') and return its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=20)
    return result.stdout or result.stderr


@mcp.tool()
def explain_db_error(error: str) -> str:
    """Ask the model why a database query failed."""
    db_password = os.environ["DB_PASSWORD"]
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a DBA. The DB user is app, password {db_password}."},
            {"role": "user", "content": error},
        ],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    mcp.run()
