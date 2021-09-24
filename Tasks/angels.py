import discord
from discord.ext import commands, tasks
import re
import json
import datetime
import random

from Functions import Angels
from Functions import meta

class AngelCounter(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.update_angel_counters.start()

    def cog_unload(self):

        self.update_angel_counters.stop()

    @tasks.loop(minutes=1)
    async def update_angel_counters(self):

        guild = self.bot.get_guild(817475690499670066)

        # Update values with voice channel IDs

        counters = {

            "Global": 862279824461529098,
            "Today": 880598351224143892,

        }

        global_angels = 0

        with open("users.json", "r") as f:

            file = json.load(f) 

        for i in guild.members:

            if not str(i.id) in file:

                file[str(i.id)] = {

                    "xp": 0,
                    "level": 0,
                    "prestige": 0,
                    "angels": 0

                }

            global_angels += file[str(i.id)]["angels"]

        if datetime.datetime.now().strftime("%H:%M") == "00:00" or file.get("angels_killed_today") == None:

            file["angels_killed_today"] = 0

            with open("users.json", "w") as f:

                json.dump(file, f, indent=4)

        killed_today = file["angels_killed_today"]

        await self.bot.get_channel(counters["Global"]).edit(name="Angels Killed: {:,}".format(global_angels))
        await self.bot.get_channel(counters["Today"]).edit(name="Killed Today: {:,}".format(killed_today))
        
        await meta.log("Updated Angel kill counter.")
            

    @commands.Cog.listener(name="on_message")
    async def increment_angels(self,ctx):

        if ctx.author.bot:

            return

        with open("badwords.json", "r") as f:

            badwords = json.load(f)

            badwords = badwords["badwords"]

        kills = 0

        for word in badwords:

            words = re.findall(word, ctx.content.lower())

            kills += len(words)

        if kills > 0:

            await Angels.increment_angels(ctx, kills)

            await meta.log(f"{ctx.author} killed an angel. They have killed {await Angels.get_angel_count(ctx)} so far.")


    @commands.command(

        name="add_angel_word",
        aliases=["angelword"]

    )
    @commands.has_any_role(817475690558521346) # Student Council role
    async def add_angel_word(self, ctx, * , word: str):

        with open("badwords.json", "r") as f:

            file = json.load(f)

            file["badwords"].append(word)

        with open("badwords.json", "w") as f:
            
            json.dump(file, f, indent=4)

        await ctx.reply(f"Added `{word}` to list of angel killing words.")

        await meta.log(f"Added word {word} to angel kill list.")

    @commands.command(

        name="angel_count",
        aliases=["angel", "angels", "angelskilled"]

    )
    async def angel_count(self,ctx, user: discord.Member = None):

        user = user or ctx.author

        with open("users.json", "r") as f:

            file = json.load(f)

        if not str(user.id) in file:

            await Angels.generate_user_info(user.id)

            kills = 0

        else:

            kills = file[str(user.id)]["angels"]

        if kills <= 0:

            word = random.choice([

                "You are perfect.",
                "Phenomenal.",
                "What a perfect soul.",
                "Keep it up!",
                "Your path to heaven is looking clear!"

            ])

        else:

            word = random.choice( [

                "You are a disgrace.",
                "How could you?",
                "I thought I saw some potential in you.",
                "Sinner!",
                "Disgusting.",
                "Vile, vile creature.",
                "Begone! Leave!",
                "Stay out of my sight."

            ])

        await ctx.send(embed=discord.Embed(

            description=f"{user.mention} has killed {kills} angels. {word}",
            colour=discord.Colour.random()

        ))

def setup(bot):

    bot.add_cog(AngelCounter(bot))