import discord
from discord.ext import commands

import random
import json

class pepega_command(commands.Cog):

    def __init__(self,bot):

        self.bot = bot

    @commands.command()
    async def pepega(self,ctx):

        with open("pepega_tracker.json", "r") as f:

            tracker = json.load(f)

        post = tracker[str(random.randint(1,len(tracker)))]

        embed = discord.Embed(

            title=f"Post by {self.bot.get_user(post['author_id'])}",
            description=f"**Author Note:** {post['content'] if post['content'] != post['link'] else None}",
            colour=discord.Colour.random()

        )

        embed.set_image(url=post['link'])

        await ctx.reply(embed=embed)

def setup(bot):

    bot.add_cog(pepega_command(bot))