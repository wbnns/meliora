from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import sqlite3

load_dotenv()

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No bot token found in environment variables.")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    conn = sqlite3.connect('discord_metrics.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (author_id, channel_id, content, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (message.author.id, message.channel.id, message.content, message.created_at))
    conn.commit()
    conn.close()

    await bot.process_commands(message)

bot.run(TOKEN)

