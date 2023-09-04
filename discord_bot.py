from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import os
import sqlite3

load_dotenv()

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No bot token found in environment variables.")

intents = discord.Intents.default()
intents.messages = False  # Indicate that we're not listening to messages
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    fetch_audit_logs.start()  # Start the periodic task

@tasks.loop(minutes=10)  # Fetch audit logs every 10 minutes, can adjust as needed
async def fetch_audit_logs():
    for guild in bot.guilds:
        audit_logs = await guild.audit_logs(limit=100).flatten()  # Fetch latest 100 entries
        for entry in audit_logs:
            conn = sqlite3.connect('discord_metrics.db')
            cursor = conn.cursor()
            # Correctly convert AuditLogAction enum to its string representation
            action_str = str(entry.action)
            # Save relevant audit log details to the database
            cursor.execute('''
                INSERT OR IGNORE INTO audit_logs (id, action, user_id, target_id, details, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (entry.id, action_str, entry.user.id, entry.target.id, str(entry.before), entry.created_at))
            conn.commit()
            conn.close()

bot.run(TOKEN)

