import discord
from discord.ext import commands, tasks
import re
import json

from Functions import Angels

class AngelCounter(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.update_angel_counters.start()

    def cog_unload(self):

        self.update_angel_counters.stop()

    @tasks.loop(minutes=5)
    async def update_angel_counters(self):

        counters = {

            "Global": 862279824461529098,
            "Today": 880598351224143892,
            "Skill210": 862647658271473664

        }

        for i in counters.items():

            channel = i[1]

            channel = self.bot.get_channel(channel)

            print(channel)

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

            print(f"{ctx.author} killed an angel. They have killed {await Angels.get_angel_count(ctx)} so far.")

def setup(bot):

    bot.add_cog(AngelCounter(bot))