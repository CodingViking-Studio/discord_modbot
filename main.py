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

rules = """
Welcome to Coding Vikings' realm!
Please read the rules and accept them in the Channel "welcome"

Rules
1. No racism or pornographic content
2. Have respect
3. No sexual harassment
4. Don't beg for higher rights
5. Not listening to Kings or Jarls can end in a permanent ban from our realm!
"""

chat_commands = {
    '/skal': 'SKAL!!',
    '/rules': rules
}

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for key in chat_commands.keys():
        if message.content.startswith(key):
            await message.channel.send(chat_commands[key])
            break

bot.run(token=r_token)
