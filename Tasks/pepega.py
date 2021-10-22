import discord
from discord.ext import commands, tasks

import os
import json
from operator import getitem
from collections import OrderedDict

from Functions import meta
from Functions import levels

# +++++++++++++++++++++++++++++++++++++++
#   Channel Configuration Variables (update as required)
pepega_channel_id = 895428130741813328
hall_of_fame_channel = 895428130385317897
guild = 895428129961684993
lb_channel = 895428130385317891
lb_message = 896989923679297556

threshold = 2

class Pepega(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.update_pepega_lb.start()

    def cog_unload(self):
        self.update_pepega_lb.stop()

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

    @tasks.loop(minutes=10)
    async def update_pepega_lb(self):

        channel = self.bot.get_channel(lb_channel)
        msg = await channel.fetch_message(lb_message)

        with open("users.json", "r") as f:
            users = json.load(f)

        res = sorted(users.items(), key=lambda x: getitem(x[1], 'pepega_posts'), reverse=True)

        embed = discord.Embed(

            title="Pepega LB",
            description="Shows who has the most pepega posts in hall of fame.",
            colour=discord.Colour.random()

        )

        for i in range(0,10):

            user_id = res[i][0]
            posts = res[i][1]['pepega_posts']

            embed.add_field(name=f"__{await self.bot.fetch_user(user_id)}__", value=posts, inline=False)

        await msg.edit(" ", embed=embed)

        await meta.log("Updated Pepega LB")

    @commands.Cog.listener(name="on_raw_reaction_add")
    async def pepega_vote_received(self, payload):

        with open("global.json", "r") as f:

            global_vars = json.load(f)

        with open("users.json", "r") as f:

            user_file = json.load(f)

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

                if i.count >= threshold:

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

                    user_file[str(message.author.id)]["pepega_posts"] += 1 

                    await self.bot.get_channel(hall_of_fame_channel).send(f"Submitted by **{message.author.mention}**",embed=embed)

                    # Add 500XP to author for entering Hall Of Fame.

                    await levels.add_xp(message.author, 500)


                    # add post to tracker

                    with open("pepega_tracker.json", "r") as f:

                        tracker = json.load(f)

                    tracker[str(len(tracker) + 1)] = {

                        "author_id": message.author.id,
                        "link": embed_url,
                        "content": message.content or None

                    }

                    with open("pepega_tracker.json", "w") as f:

                        json.dump(tracker, f, indent=4)

                    # write data to global and user file

                    with open("global.json", "w") as f:

                        json.dump(global_vars, f, indent=4)
                    
                    with open("users.json", "w") as f:

                        json.dump(user_file, f, indent=4)

                    await meta.log(f"Pepega post by {message.author} has entered Hall of Fame.")


            elif i.emoji == "❌":

                if i.count == threshold:

                    await message.add_reaction("⛔")

                    await meta.log(f"Pepega post by {message.author} blocked.")





def setup(bot):
    bot.add_cog(Pepega(bot))