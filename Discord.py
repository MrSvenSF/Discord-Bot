#import importlib
import discord
import os 
from dotenv import load_dotenv
import yaml

bot = discord.Bot()


# on_ready event
@bot.event
async def on_ready():
    print(f"Online ---------------------------------------")
    print(f"{bot.user} is ready and online!")
    print(f"")
# end on_ready event


# Load .env (token)
load_dotenv(dotenv_path="config/.env")
token = os.getenv("token")
if not token:
    print("-------Token-Error-------")
    print("Token not found in config/.env file. Please set the token.")
    print("create a .env file in the config folder with the following content:")
    print("token=<your_token_here>")
    print("exiting...")
    exit(1)
# end Load .env (token)


# test command
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")
# end test command


bot.run(os.getenv("token"))

# --- start of module loading ---
#config_path = "config/config.yml"

#with open(config_path, "r", encoding="utf-8") as f:
#    config = yaml.safe_load(f)

#for key, enabled in config.items():
#    if isinstance(enabled, bool) and enabled:
#        module_path = config.get("in", {}).get(key)
#        if module_path and os.path.exists(module_path):
#            spec = importlib.util.spec_from_file_location(key, module_path)
#            module = importlib.util.module_from_spec(spec)
#            spec.loader.exec_module(module)
#            print("-------------Modul-load-------------")
#            print(f"Modul {module_path} geladen.")
#            print("")
#        elif module_path:
#            print("-------------Modul-Error-------------")
#            print(f"Modul {module_path} nicht gefunden.")
#            print("")

# --- end of module loading ---