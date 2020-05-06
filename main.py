from datetime import datetime
import os

import discord


BOT_TOKEN = os.getenv("PYTHON_BOT_TOKEN", "")


def main():
    print(f"Hello world! Now is {datetime.now()}")
    print(f"discord.py version {discord.__version__}")
    if BOT_TOKEN:
        print("Got token from sys env")
    else:
        print("Not token found in sys env")


if __name__ == "__main__":
    main()
