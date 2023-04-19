import os, pathlib
import requests, json

APPLICATION_ID  = os.getenv("MINIAPP_ID")
BOT_TOKEN       = os.getenv("MINIBOT_TOKEN")
DISCORD_COMMAND_URL = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"

if APPLICATION_ID is None or BOT_TOKEN is None:
  print("Please set the environment variables MINIAPP_ID and MINIBOT_TOKEN")
  exit(1)

headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

commands_directory = pathlib.Path(__file__).parent.absolute() / "commands"

for file in commands_directory.glob("*.json"):
    with open(file, "r") as f:
      command_config = json.load(f)
      r = requests.post(DISCORD_COMMAND_URL, headers=headers, json=command_config)
      print(r.status_code)
      print(r.text)