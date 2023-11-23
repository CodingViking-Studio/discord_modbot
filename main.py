import json
import discord

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


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1133683869317595186))
    print(f"We have logged in as {bot.user}")


@tree.command(name="skal", description="Greet Ubba!")
async def skal(interaction):
    await interaction.response.send_message(f"SKAL, {interaction.user}!!")


@tree.command(name="rules", description="Get all current rules")
async def rules(interaction):
    await interaction.response.send_message(main_rules)


@bot.event
async def on_message(message):
    if message.content.startswith("/update_tree"):
        print("Updating commandtree")
        await tree.sync(guild=discord.Object(id=1133683869317595186))


bot.run(token=r_token)
