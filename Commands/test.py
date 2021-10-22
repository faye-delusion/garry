import discord
from discord.ext import commands

from Functions import Angels
from Functions import levels

# I USE THIS FOR TESTING SHIT
# IT IS NOT A FEATURE

class test(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="test")
    @commands.is_owner()
    async def test(self,ctx):

        await levels.get_xp_multiplier(ctx.author)


def setup(bot):
    bot.add_cog(test(bot))