import os

import discord

GUILD_NAME = "Patlabor"
BOT_TOKEN = os.getenv("PYTHON_BOT_TOKEN", "")


class MyClient(discord.Client):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD_NAME)
        print(f"{self.user} has connected to guild: {guild.name}({guild.id})")

    async def on_message(self, message):
        if message.author == self.user:
            print("I'm not gonna answer myself")
            return

        if message.content == "ping":
            await message.channel.send("pong")
        else:
            await message.channel.send("Sorry but I don't understand your message...")


def main():
    client = MyClient()
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
