import discord
from discord.ext import commands

aliases = []

class whois(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="whois", aliases=aliases)
    async def whois(self,ctx, user: discord.User = None):

        user = user or ctx.author

        embed = discord.Embed(

            title=f"{user.name}",
            colour=discord.Colour.random()

        )

        embed.set_image(url=user.avatar_url)

        if user.activities:

            for i in user.activities:
                
                if i.type == discord.ActivityType.custom:

                    embed.add_field(

                        name=f"Custom Status",
                        value=f"**Notification Setting:** {i.state}\n**Text:** {i}\n**Since:** <t:{int(i.created_at.timestamp())}>",
                        inline=False

                    )

                    

        embed.add_field(

            name="Name", 
            value=user
            
        )

        embed.add_field(
            
            name="Account Creation Date", 
            value=f"<t:{int(user.created_at.timestamp())}>"
            
        )

        await ctx.reply(embed=embed)

def setup(bot):

    bot.add_cog(whois(bot))