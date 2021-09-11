import json

async def get_angel_count(ctx):

    with open("users.json", "r") as f:

        file = json.load(f)

    if not str(ctx.author.id) in file:

        file[str(ctx.author.id)] = {

            "xp": 0,
            "level": 0,
            "prestige": 0,
            "angels": 0

        }

        with open("users.json", "w") as f:

            json.dump(file, f, indent=4)

    return file[str(ctx.author.id)]["angels"]
