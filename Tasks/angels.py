import discord
from discord.ext import commands, tasks

from Functions import Angels

class AngelCounter(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name="on_message")
    async def increment_angels(self,ctx):

        await Angels.increment_angels(ctx, 1)

        print(f"{await Angels.get_angel_count(ctx)}")

def setup(bot):

    bot.add_cog(AngelCounter(bot))