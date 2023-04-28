import discord
import os

MINIBOT_TOKEN = os.getenv('MINIBOT_TOKEN')
if MINIBOT_TOKEN is None:
    raise ValueError('MINIBOT_TOKEN environment variable not set')

intents = discord.Intents().default()
intents.message_content = True

bot = discord.Bot(intents=intents)

import whisper

print("loading model...")
model = whisper.load_model("large")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments and message.attachments[0].filename == "voice-message.ogg":
        await message.channel.send("received your voice message: " + "\n".join(map(lambda x: x.url, message.attachments)))
        print("writing voice message to file...")
        await message.attachments[0].save("voice-message.ogg")
        print("transcribing voice...")
        result = model.transcribe("voice-message.ogg", timestamps=True, fp16=False)

        # transcribe and return timestamps
        print("sending message...")
        await message.channel.send(result.get("text", "no text found"))

bot.run(MINIBOT_TOKEN)