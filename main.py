import sys

import discord

from bot import BOT_TOKEN


def main():
    print(f"python version: {sys.version}")
    print(f"discord.py version {discord.__version__}")

    if not BOT_TOKEN:
        raise Exception("No token found in sys env")

    print("Got token from sys env")


if __name__ == "__main__":
    main()
