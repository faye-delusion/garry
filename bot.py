# hey jack
import json
import os

import discord
from discord.ext import commands
from discord_components import DiscordComponents


# Open config file, stores values and stuff

with open("./config.json", "r") as f:

    config = json.load(f)


# generates badwords.json if it doesnt already exist

try:

    open("badwords.json")

except:

    with open("badwords.json", "w") as f:

        json.dump({"badwords": []}, f, indent=4)


# Init the actual bot

intents = intents = discord.Intents.all()

bot = commands.Bot(
    
    command_prefix = config["prefix"], 
    case_insensitive = True, 
    intents = intents, 
    help_command = None
    
)

log_channel = discord.TextChannel

# Initialise shit when the bot is loaded.

@bot.event
async def on_ready():

    # Write to log_channel variable

    log_channel = bot.get_channel(config["log_channel"])

    # Load commands

    for command in os.listdir("./Commands"):

        if command.endswith(".py"):

            try:

                bot.load_extension(f"Commands.{command[:-3]}")

            except commands.ExtensionAlreadyLoaded:

                print(f"Command {command[:-3]} already loaded")

            except commands.NoEntryPointError:

                print(f"Command {command[:-3]} has no setup function")

            except commands.ExtensionFailed:

                print(f"Command {command[:-3]} threw an exception and could not be loaded")

            else:

                print(f"Command {command[:-3]} loaded successfully")

        for task in os.listdir("./Tasks"):

            if task.endswith(".py"):

                try:

                    bot.load_extension(f"Tasks.{task[:-3]}")

                except commands.ExtensionAlreadyLoaded:

                    print(f"Task {task[:-3]} already loaded")

                except commands.NoEntryPointError:

                    print(f"Task {task[:-3]} has no setup function")

                except commands.ExtensionFailed:

                    print(f"Task {task[:-3]} threw an exception and could not be loaded")

                else:

                    print(f"Task {task[:-3]} loaded successfully")

        embed = discord.Embed(

            title="Garry Restarted",
            colour=discord.Colour.random()

        )

    await log_channel.send(embed=embed)

# Run the bot

DiscordComponents(bot)
bot.run(config["token"], reconnect = True)