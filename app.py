"""Tiny Flask demo service used as AEGIS's monitored target. Intentionally minimal."""
from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
