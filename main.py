import json
import discord
from setup import configured_messages
from random import randint
from discord.ext import commands
from random import randint
from databases import gen_db

a_intents = discord.Intents.default()
a_intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=a_intents,
                   case_insensitive=False,)

try:
    with open("config.json", "r") as f:
        content = json.load(f)
        r_token = content["discord_token"]
        bn = content['bot_name']
        rules_channel_id = 1135190464484606035
        server_id = 1133683869317595186
except:
    raise

msg_db = gen_db('resources/{bn}.db')

# Generate entries on First start
if len(msg_db.get_all_msgs()) < 1:
    for msg_data  in configured_messages():
        msg_db.add_msg(msg_data)

pfp_path = "./data/profilepic_{bn}.jpg"

fp = open(pfp_path, 'rb')
pfp = fp.read()

rt = {
    "elter_furthark": {
            "text2runes": {
                "A": "ᚨ",
                "B": "ᛒ",
                "C": "ᚲ",
                "D": "ᛞ",
                "E": "ᛖ",
                "F": "ᚠ",
                "G": "ᚷ",
                "H": "ᚺ",
                "I": "ᛁ",
                "J": "ᛃ",
                "K": "ᚲ",
                "L": "ᛚ",
                "M": "ᛗ",
                "N": "ᚾ",
                "O": "ᛟ",
                "P": "ᛈ",
                "Q": "ᚲ",
                "R": "ᚱ",
                "S": "ᛊ",
                "T": "ᛏ",
                "U": "ᚢ",
                "V": "ᚢ",
                "W": "ᚹ",
                "X": "ᚲᛊ",
                "Y": "ᛁ",
                "Z": "ᛉ"
            },
            "runes2text":{
                "ᚨ": "A",
                "ᛒ": "B",
                "ᚲ": "C",
                "ᛞ": "D",
                "ᛖ": "E",
                "ᚠ": "F",
                "ᚷ": "G",
                "ᚺ": "H",
                "ᛁ": "I",
                "ᛃ": "J",
                "ᚲ": "K",
                "ᛚ": "L",
                "ᛗ": "M",
                "ᚾ": "N",
                "ᛟ": "O",
                "ᛈ": "P",
                "ᚲ": "Q",
                "ᚱ": "R",
                "ᛊ": "S",
                "ᛏ": "T",
                "ᚢ": "U",
                "ᚢ": "V",
                "ᚹ": "W",
                "ᚲᛊ": "X",
                "ᛁ": "Y",
                "ᛉ": "Z"
            }
        }
    }

ef_t2r = rt["elter_furthark"]["text2runes"]
ef_r2t = rt["elter_furthark"]["runes2text"]


main_rules = msg_db.get_msg("main_rules")[-1]

mc_server_info = msg_db.get_msg("mcs_info")[-1]


def drinking_greets(username):
    dg = [
        f"SKÅL, {username}!!",
        "To you my brother!",
        f"You fought well in our last battle {username}, skål!",
        "Anotherone ?, lets see who lasts longer!",
        f"Look at {username}, he is completly drunk again"
    ]
    return dg[randint(0, len(dg))]


@bot.event
async def on_ready():
    await bot.user.edit(avatar=pfp)
    print(f"We have logged in as {bot.user}")
    if main_rules["message_id"] == "":
        msg = rules_channel_id.send_message(main_rules["content"])
        print("send", msg.id)
    else:
        print('fetched', rules_channel_id.fetch_message(main_rules["message_id"]))

@bot.tree.command(name="skal", description="Greet Ubba!")
async def skal(interaction: discord.Interaction):
    await interaction.response.send_message(drinking_greets(interaction.user))


@bot.tree.command(name="rules", description="Get all current rules")
async def rules(interaction: discord.Interaction):
    await interaction.response.send_message(main_rules)


@bot.tree.command(name="minecraft", description="Get all Minecraft serverdata")
async def minecraft(interaction: discord.Interaction):
    await interaction.response.send_message(mc_server_info)


@bot.tree.command(name="mc_whitelist", description="Manipulate the Whitelist of the Minecraft server")
@discord.app_commands.choices(option=[
    discord.app_commands.Choice(name='add', value=1),
    discord.app_commands.Choice(name='remove', value=2)
])
async def mc_whitelist(interaction: discord.Interaction, name: str, option: discord.app_commands.Choice[int]):
    if interaction.user.id == 224515637291122688 or 'King' in interaction.user.roles[-1].name:
        match option.value:
            case 1:
                await interaction.response.send_message(f"The user {name} has been added")
            case 2:
                await interaction.response.send_message(f"The user {name} has been removed")
            case _:
                pass
    else:
        await interaction.response.send_message("You got no permission to execute this command!")


@bot.tree.command(name="translate", description="Get your text translated to the elder furthark")
async def translator(interaction: discord.Interaction, txt: str):
    translated = [(ef_t2r[c.upper()]) if c.upper() in ef_t2r.keys() else (c) for c in txt]
    await interaction.response.send_message("".join(translated))


@bot.tree.command(name="test", description="testo")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("test")


@bot.command()
async def sync(interaction: discord.Interaction):
    print("sync commands")
    if interaction.author.id == 224515637291122688:
        # Remove Guild specific, when not used anymore! Only DEBUG
        bot.tree.copy_global_to(guild=discord.Object(id=server_id))
        # synced = await bot.tree.sync(guild=discord.Object(id=1133683869317595186))
        synced = await bot.tree.sync()
        await interaction.send(f'Command tree synced ({len(synced)} commands). It can take up to an hour to sync all commands')
    else:
        await interaction.send('You must be the owner to use this command!')
    return

bot.run(token=r_token)
