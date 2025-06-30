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

load_dotenv(dotenv_path="Config/.env")
load_dotenv(dotenv_path=".env")
token = os.getenv("token")

bot.run(token)
