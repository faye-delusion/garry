import discord
from discord.ext import commands, tasks

import os
import json

from Functions import meta

# +++++++++++++++++++++++++++++++++++++++
#   Channel Configuration Variables (update as required)
pepega_channel_id = 895428130741813328
hall_of_fame_channel = 895428130385317897
guild = 895428129961684993

class Pepega(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener(name="on_message")
    async def create_pepega_post(self,message):

        if message.author.bot:

            return

        if message.channel.id == pepega_channel_id:

            if len(message.embeds) > 0:

                if message.embeds[0].type != "image":

                    return

                await meta.log(f"Pepega Post Created by {message.author}")

            elif len(message.attachments) > 0:

                await meta.log(f"Pepega Post Created by {message.author}")

            else:

                return

            for i in ["✅", "❌"]:

                await message.add_reaction(i)

    @commands.Cog.listener(name="on_raw_reaction_add")
    async def pepega_vote_received(self, payload):

        with open("global.json", "r") as f:

            global_vars = json.load(f)

        if not payload.channel_id == pepega_channel_id or payload.guild_id != guild:

            return

        reacter_id = payload.user_id
        message_id = payload.message_id

        pepega_channel = await self.bot.fetch_channel(payload.channel_id)

        message = await pepega_channel.fetch_message(message_id)

        reacter = await self.bot.fetch_user(reacter_id)

        if reacter.bot:

            return

        if not str(payload.emoji) in ["✅", "❌"]:

            return

        await meta.log(f"{reacter} added {payload.emoji} reaction to {message.author}'s Pepega Post")

        for i in message.reactions:

            if i.emoji == "⭐" or i.emoji == "⛔":

                if i.me:

                    return

        for i in message.reactions:

            if i.emoji == "✅":

                if i.count >= 2:

                    await message.add_reaction("⭐")

                    if message.attachments:

                        embed_url = message.attachments[0].url

                    elif message.embeds:

                        for i in message.embeds:

                            if i.type == "image":

                                embed_url = i.url

                    embed = discord.Embed(

                        title=f"Pepega #{global_vars['pepega_count']}",
                        colour=discord.Colour.random()

                    )

                    embed.set_image(url=embed_url)

                    global_vars['pepega_count'] += 1

                    await self.bot.get_channel(hall_of_fame_channel).send(f"Submitted by **{message.author.mention}**",embed=embed)

                    with open("global.json", "w") as f:

                        json.dump(global_vars, f, indent=4)



                    




            

def setup(bot):
    bot.add_cog(Pepega(bot))