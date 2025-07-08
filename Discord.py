import discord
import os
from dotenv import load_dotenv
import yaml

bot = discord.Bot()
loaded_cogs = set()

@bot.event
async def on_ready():
    print(f"Online ---------------------------------------")
    print(f"{bot.user} is ready and online!")
    print(f"")
    
load_dotenv(dotenv_path="Config/.env")
token = os.getenv("token")
if not token:
    print("-------Token-Error-------")
    print("Token not found in .env file. Please set the token.")
    print("create a .env file in the Config folder with the following content:")
    print("token=<your_token_here>")
    print("exiting...")
    exit(1)


with open("Config/config-Tools.yml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
for key, enabled in config.items():
    if key == "in":
        continue
    if isinstance(enabled, bool) and enabled:
        ext_path = config.get("in", {}).get(key)
        if ext_path and key not in loaded_cogs:
            try:
                bot.load_extension(ext_path)
                loaded_cogs.add(key)
            except Exception as e:
                print(f"Fehler beim Laden von {ext_path}: {e}")



bot.run(os.getenv("token"))