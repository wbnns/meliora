from flask import Flask, render_template
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    conn = sqlite3.connect('discord_metrics.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM audit_logs ORDER BY timestamp DESC')
    audit_logs = cursor.fetchall()
    conn.close()

    return render_template('audit_metrics.html', audit_logs=audit_logs)

if __name__ == "__main__":
    app.run(debug=True)

