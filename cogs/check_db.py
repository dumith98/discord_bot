import discord
import os
from DatabaseConnections.PostgresConnection import PostgresConnection
from discord.ext import commands
import dotenv


class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("List command has loaded successfully!")
        message = random_info.CheckUser()
        print(message)

    @commands.command()
    async def list(self, ctx):
        dotenv.load_dotenv()
        postgres = PostgresConnection(
            os.getenv("database"),
            os.getenv("user"),
            os.getenv("password"),
            os.getenv("host"),
        )
        await ctx.send(f"{postgres.getAllNames()}")


async def setup(bot):
    await bot.add_cog(List(bot))
