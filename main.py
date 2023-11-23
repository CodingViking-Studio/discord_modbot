import json
import discord
from random import randint

test = ""

a_intents = discord.Intents.default()
a_intents.message_content = True

bot = discord.Client(intents=a_intents)
tree = discord.app_commands.CommandTree(bot)


try:
    with open("config.json", "r") as f:
        content = json.load(f)
        r_token = content["discord_token"]
except:
    raise


main_rules = """
Welcome to Coding Vikings' realm!
Please read the rules and accept them in the Channel "welcome"

Rules
1. No racism or pornographic content
2. Have respect
3. No sexual harassment
4. Don't beg for higher rights
5. Not listening to Kings or Jarls can end in a permanent ban from our realm!
"""

mc_server_info = """
Want to play on our own Server ?

Here you go! Ask a King for permission and get Whitelistet.

IP:

Rules
1. No griefing
2. No killig of other players (Outside of official events or with consent of your opponent!)
3. Please leave room between your Builds. (Estimated Radius of 500 Blocks)
4. We want an medieval Server theme, so please only build in this style too
5. If you want to build a Farm or need one, message a King or Jarl first. Maybe there is
   already one. If you are the First, please build it somewhere, where everyone can use it!
"""


def drinking_greets(username):
    drinking_greets = [
        f"SKÅL, {username}!!",
        f"To you my brother!",
        f"You fought well in our last battle {username}, skål!",
        f"Anotherone ?, lets see who last longer!",
        f"Look at {username}, he is completly drunk again"
    ]
    return drinking_greets[randint(0, len(drinking_greets))]


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1133683869317595186))
    print(f"We have logged in as {bot.user}")


@tree.command(name="skal", description="Greet Ubba!")
async def skal(interaction):
    await interaction.response.send_message(drinking_greets(interaction.user))


@tree.command(name="rules", description="Get all current rules")
async def rules(interaction):
    await interaction.user.send(main_rules)


@tree.command(name="minecraft", description="Get all Minecraft serverdata")
async def rules(interaction):
    await interaction.user.send(mc_server_info)


@tree.command(name="mc_whitelist", description="Manipulate the Whitelist of the Minecraft server")
async def rules(interaction, name: str, option: str):
    if interaction.user.permission == "Admin":
        case option:
            "add":
                await interaction.user.send(f"The user {name} has been added")
            "remove":
                await interaction.user.send(f"The user {name} has been removed")
            _:
                pass
    else
        await interaction.user.send("You got no permission to execute this command!")


@bot.event
async def on_message(message):
    if message.content.startswith("/update_tree"):
        print("Updating commandtree")
        await tree.sync(guild=discord.Object(id=1133683869317595186))


bot.run(token=r_token)
