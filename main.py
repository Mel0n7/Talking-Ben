from http.client import responses
import discord, os, discord.ext, random
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.playing, name="Talking Ben")
  await client.change_presence(activity=activity)
  print("Bot Online")

@client.event
async def on_message(message):
    if message.content.startswith("Ben") or message.content.startswith("ben") or client.user.mentioned_in(message):
        responses = ["Yes", "No", "Hohoho", "Uhh"]
        await message.reply(f"{random.choice(responses)}")

client.run(os.getenv("TOKEN"))

# https://discord.com/api/oauth2/authorize?client_id=956790001578958878&permissions=2048&scope=bot