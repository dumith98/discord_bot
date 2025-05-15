import discord
import os
from DatabaseConnections.PostgresConnection import PostgresConnection
from discord.ext import commands
import dotenv
from loguru import logger


class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("List command has loaded successfully!")

    @commands.command()
    async def list(self, ctx):
        dotenv.load_dotenv()
        postgres = PostgresConnection(
            os.getenv("database"),
            os.getenv("user"),
            os.getenv("password"),
            os.getenv("host"),
        )
        await ctx.send(f"{postgres.getAllNames('user_table')}")


async def setup(bot):
    await bot.add_cog(List(bot))
