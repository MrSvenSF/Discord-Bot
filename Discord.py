import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import yaml
import importlib.util

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"-------------Online-------------")
    print(f"")

load_dotenv(dotenv_path="Config/.env")
token = os.getenv("token")
if not token:
    print("-------Token-Error-------")
    print("Token not found in .env file. Please set the token.")
    print("token=<your_token_here>")
    print("exiting...")
    exit(1)

config_path = "Config/config.yml"
if not os.path.exists(config_path):
    print("-------------Config-Error-------------")
    print("Config/config.yml not found. Please create it.")
    print("exiting...")
    exit(1)



# --- start of module loading ---
with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

for key, enabled in config.items():
    if isinstance(enabled, bool) and enabled:
        module_path = config.get("in", {}).get(key)
        if module_path and os.path.exists(module_path):
            spec = importlib.util.spec_from_file_location(key, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print("-------------Modul-load-------------")
            print(f"Modul {module_path} geladen.")
            print("")
        elif module_path:
            print("-------------Modul-Error-------------")
            print(f"Modul {module_path} nicht gefunden.")
            print("")

# --- end of module loading ---


bot.run(token)

