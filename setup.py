"""
Main Initial Setup Data for Variables
"""
import json

def furthark_translation() -> dict:
    return {
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

def configured_messages() -> list:
    return [
        {
            "id": "",
            "name": "main_rules",
            "content": """
            Welcome to Coding Vikings' realm!
            Please read the rules and accept them in the Channel 'welcome'
            
            Rules
            1. No racism or pornographic content
            2. Have respect
            3. No sexual harassment
            4. Don't beg for higher rights
            5. Not listening to Kings or Jarls can end in a permanent ban from our realm!
            """
        },
        {
            "id": "",
            "name": "mcs_info",
            "content": """
            Minecraft server Rules
            
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
        }
    ]

def discord_server_connection() -> list:
    """Returns the Data out of Config File

    Returns:
        list: r_token; bot_name; rules_channel_id; server_id
    """
    try:
        with open("config.json", "r") as f:
            content = json.load(f)
            r_token = content["discord_token"]
            bot_name = content['bot_name']
            rules_channel_id = 1135190464484606035
            server_id = 1133683869317595186
    except:
        raise

    return r_token, bot_name, rules_channel_id, server_id