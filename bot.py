""" Bot definition """

import logging
import os

import discord

GUILD_NAME = "Patlabor"
BOT_TOKEN = os.getenv("PYTHON_BOT_TOKEN", "")

LOGGER = logging.getLogger(__name__)


class MyClient(discord.Client):
    """Client which communicates with Discord service"""

    async def on_ready(self):
        """ready hook"""

        guild = discord.utils.get(self.guilds, name=GUILD_NAME)
        LOGGER.info(
            "%s has connected to guild: %s(%s)" % (self.user, guild.name, guild.id)
        )

    async def on_message(self, message):
        """message hook"""

        if message.author == self.user:
            return

        LOGGER.info("Message received from %s: %s" % (message.author, message.content))

        if message.content == "ping":
            await message.channel.send("pong")
        else:
            await message.channel.send("Sorry but I cannot understand your message...")


intents = discord.Intents.default()
intents.message_content = True


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
    )
    client = MyClient(intents=intents)
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
