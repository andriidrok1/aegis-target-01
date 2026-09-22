"""Create users.db with a few demo rows."""
import sqlite3

conn = sqlite3.connect("users.db")
conn.executescript(open("schema.sql").read())
conn.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
                 [("ada", "ada@example.com"), ("linus", "linus@example.com"), ("grace", "grace@example.com")])
conn.commit()
print("seeded", conn.execute("SELECT count(*) FROM users").fetchone()[0], "users")
