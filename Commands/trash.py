import discord
from discord.ext import commands

class trash(commands.Cog):

    def __init__(self,bot):

        self.bot = bot


    @commands.command(name="trash")
    async def trash(self,ctx):

        await ctx.send("SHUT THE FUCK UP")

def setup(bot):
    
    bot.add_cog(trash(bot))