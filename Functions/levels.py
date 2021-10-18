import json
import discord

from Functions import meta

async def generate_user_profile(user: discord.User):

    with open("users.json", "r") as f:

        file = json.load(f)

    if str(user.id) in file:

        return

    else:

        file[str(user.id)] = {

            "xp": 0,
            "level": 1,
            "prestige": 0,
            "angels_killed": 0,
            "pepega_posts": 0

        }


async def add_xp(xp_amount: int, user: discord.User):

    with open("users.json", "r") as f:

        file = json.load(f)

    if not user.id in file:

        generate_user_profile(user)