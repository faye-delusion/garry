# Setup file (only run once)

import os
import json

if not os.path.isfile("config.json"):

    print("Generating config file")

    token = str(input("Enter bot token:\t"))

    prefix = input("Enter prefix to use (g2 = default):\t")

    prefix = prefix or "g2"

    logchannel = int(input("Enter ID for channel to post logs:\t"))

    with open("config.json", "w") as f:

        json.dump(

            {"token": token, "prefix": prefix, "log_channel": logchannel},
            f,
            indent=4

        )

    print("Config generated (see config.json)")

if not os.path.isfile("badwords.json"):

    print("Generating badwords.json file (used for angels)")

    with open("badwords.json", "w") as f:

        json.dump(

            {"badwords": [
                "fuck",
                "shit",
                "pussy",
                "cunt",
                "omg",
                "omfg",
                "gay",
                "balls",
                "crotch",
                "testicles",
                "nuts",
                "heck",
                "hell",
                "tf",
                "ned",
                "punk",
                "bitch",
                "arse",
                "retard",
                "ass",
                "tit",
                "boob",
                "piss",
                "horny",
                "pee",
                "kink",
                "butt",
                "bum",
                "tramp",
                "jerk",
                "porn",
                "fag",
                "slut",
                "shart",
                "crap",
                "poo",
                "fart",
                "sex",
                "nigg",
                "cock",
                "prick",
                "wench",
                "whore",
                "bastard",
                "dick",
                "slag"]},
            f,
            indent=4

        )

    print("Badwords generated with default words (see badwords.json)")

if not os.path.isfile("users.json"):

    print("Generating user data file")

    with open("users.json", "w") as f:

        json.dump(

            {"angels_killed_today": 0},
            f,
            indent=4

        )

    print("Users generated (see users.json)")

if not os.path.isfile("global.json"):

    print("Generating global.json variable file")

    with open("global.json", "w") as f:

        json.dump(

            {

                "angels_killed_today": 0,
                "pepega_count": 0

            },
            f,
            indent=4

        )

if not os.path.isfile("pepega_tracker.json"):

    print("Generating pepega tracker")

    with open("pepega_tracker.json", "w") as f:

        json.dump(

            {},
            f,
            indent=4

        )

print("Setup complete. Run bot.py to start bot.")