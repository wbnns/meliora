import sqlite3

conn = sqlite3.connect('discord_metrics.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    author_id TEXT NOT NULL,
    channel_id TEXT NOT NULL,
    content TEXT,
    timestamp TEXT NOT NULL
)
''')

conn.commit()
conn.close()

