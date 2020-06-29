from datetime import datetime

import discord

from bot import BOT_TOKEN


def main():
    print(f"Hello world! Now is {datetime.now()}")
    print(f"discord.py version {discord.__version__}")
    if BOT_TOKEN:
        print("Got token from sys env")
    else:
        print("No token found in sys env")


if __name__ == "__main__":
    main()
