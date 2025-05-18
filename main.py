import asyncio
import os
import discord
import strutlog
from discord.app_commands import command
from discord.ext import commands
from dotenv import load_dotenv

logger = strutlog.get_logger()


def main() -> None:
    load_dotenv()

    TOKEN = os.getenv("DISCORD_TOKEN")

    bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

    async def Load():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")

    async def main():
        async with bot:
            await Load()
            await bot.start(TOKEN)

    @bot.event
    async def on_ready():
        logger.info(f"\n{bot.user.name} has connected successfully!")

    asyncio.run(main())


if __name__ == "__main__":
    main()
