import json
import discord

a_intents = discord.Intents.default()
a_intents.message_content = True

bot = discord.Client(intents=a_intents)

try:
    with open("config.json", "r") as f:
        content = json.load(f)
        r_token = content["discord_token"]
except:
    raise

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('/skal'):
        await message.channel.send(f'SKAL, {message.author}!!')

bot.run(token=r_token)
