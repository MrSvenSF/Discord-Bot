import discord
import os 
from dotenv import load_dotenv
import yaml

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Online ---------------------------------------")
    print(f"{bot.user} is ready and online!")
    print(f"")
    
load_dotenv(dotenv_path="config/.env")
token = os.getenv("token")
if not token:
    print("-------Token-Error-------")
    print("Token not found in config/.env file. Please set the token.")
    print("create a .env file in the config folder with the following content:")
    print("token=<your_token_here>")
    print("exiting...")
    exit(1)
    
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(os.getenv("token"))