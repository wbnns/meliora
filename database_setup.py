import sqlite3

conn = sqlite3.connect('discord_metrics.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY,
    action TEXT NOT NULL,
    user_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    details TEXT,
    timestamp TEXT NOT NULL
)
''')

conn.commit()
conn.close()

