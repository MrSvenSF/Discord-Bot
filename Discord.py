#import importlib
import discord
import os 
from dotenv import load_dotenv
import json

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

#---------------------------------------------------------------------------------------------------------------

# Load config (JSON)
config_path = "config/config.json"
if not os.path.exists(config_path):
    print("-------Config-Error-------")
    print(f"Config-Datei {config_path} nicht gefunden.")
    print("Bitte erstelle eine config/config.json (siehe config/config.json.example).")
    print("exiting...")
    exit(1)

with open(config_path, "r", encoding="utf-8") as f:
    try:
        config = json.load(f)
    except Exception as e:
        print("-------Config-Error-------")
        print(f"Fehler beim Lesen der JSON-Konfiguration: {e}")
        print("exiting...")
        exit(1)

modules_cfg = config.get("modules", [])

import importlib.util

# Lade Module, deren Einträge in config/config.yml aufgelistet sind.
# Die Pfade werden relativ zur config-Datei aufgelöst.
for mod in modules_cfg:
    name = mod.get("name")
    enabled = mod.get("enabled", False)
    path = mod.get("path")

    if not enabled:
        continue

    if not path:
        print("-------------Modul-Error-------------")
        print(f"Modul {name} hat keinen Pfad; übersprungen.")
        print("")
        continue

    # Pfad relativ zur config.yml auflösen
    module_path = os.path.normpath(os.path.join(os.path.dirname(config_path), path))

    if not os.path.exists(module_path):
        print("-------------Modul-Error-------------")
        print(f"Modul {module_path} nicht gefunden.")
        print("")
        continue

    try:
        spec = importlib.util.spec_from_file_location(name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Wenn das Modul eine setup(bot)-Funktion hat, rufe sie auf
        if hasattr(module, "setup"):
            try:
                module.setup(bot)
                print("-------------Modul-load-------------")
                print(f"Modul {module_path} geladen via setup().")
                print("")
            except Exception as e:
                print("-------------Modul-Error-------------")
                print(f"Fehler beim Ausführen von setup() in {module_path}: {e}")
                print("")
        else:
            print("-------------Modul-load-------------")
            print(f"Modul {module_path} geladen (keine setup()-Funktion).")
            print("")
    except Exception as e:
        print("-------------Modul-Error-------------")
        print(f"Fehler beim Laden von {module_path}: {e}")
        print("")

#---------------------------------------------------------------------------------------------------------------

bot.run(token)