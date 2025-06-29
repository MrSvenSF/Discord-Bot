import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"-------online-------")
    print(f"  {bot.user.name}")
    print(f"")

# Versuche zuerst ../Config/.env, dann .env im aktuellen Verzeichnis
load_dotenv(dotenv_path="src/.env")
load_dotenv(dotenv_path=".env")

token = os.getenv("token")

bot.run(token)

