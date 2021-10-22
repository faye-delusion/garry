import discord
from discord.ext import commands

import json

aliases = [

    "lvl",
    "r",
    "level",
    "lv"

]

class rank(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command(aliases=aliases)
    async def rank(self,ctx,user: discord.User = None):

        user = user or ctx.author

        with open("users.json", "r") as f:

            file = json.load(f)

        xp = file[str(user.id)]["xp"]
        level = file[str(user.id)]["level"]
        prestige = file[str(user.id)]["prestige"]

        if level >= 50:

            xp_to_rankup = 50 * 200

        else:

            xp_to_rankup = file[str(user.id)]["level"] * 200 


        embed = discord.Embed(

            title=f"{user.name}"

        )

        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(rank(bot))