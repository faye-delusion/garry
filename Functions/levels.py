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

async def get_xp_multiplier(user:discord.User):

    with open("users.json", "r") as f:

        file = json.load(f)

    xp_multi = 1.0 # default

    # Standard Multipliers (Pepega, Prestige, etc)

    xp_multi += file[str(user.id)]["prestige"]
    xp_multi += file[str(user.id)]["pepega_posts"] / 100

    # Nitro Boost Multiplier

    for role in user.roles:

        if role.is_premium_subscriber(): # Nitro role omegalul

            xp_multi += 0.75


    # Dream Mask Multiplier

    for activity in user.activities:

        if type(activity) == discord.Spotify:

            # Track ID for Dream's beloved song Mask

            if activity.track_id == "3IxMaULfjq4IT2IN6v54PB":

                xp_multi += 1 

    




async def add_xp(xp_amount: int, user: discord.User):

    with open("users.json", "r") as f:

        file = json.load(f)

    if not user.id in file:

        generate_user_profile(user)

    # Do xp multiplier shite yada yada fuck off







    file[str(user.id)]["xp"] += xp_amount

    with open("users.json", "r") as f:

        json.dump(file, f, indent=4)

    await meta.log(f"{xp_amount} added to {user}")