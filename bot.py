import logging
import os

import discord

GUILD_NAME = "Patlabor"
BOT_TOKEN = os.getenv("PYTHON_BOT_TOKEN", "")

LOGGER = logging.getLogger(__name__)


class MyClient(discord.Client):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD_NAME)
        LOGGER.info(f"{self.user} has connected to guild: {guild.name}({guild.id})")

    async def on_message(self, message):
        if message.author == self.user:
            return

        LOGGER.info(f"Message received from {message.author}")

        if message.content == "ping":
            await message.channel.send("pong")
        else:
            await message.channel.send("Sorry but I don't understand your message...")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
    )
    client = MyClient()
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
