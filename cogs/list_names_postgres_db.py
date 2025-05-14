from typing import TypedDict

from psycopg2 import DatabaseError
import discord
import os
from DatabaseConnections.PostgresConnection import PostgresConnection
from discord.ext import commands
import dotenv


class DataBaseConfig(TypedDict):
    database: str
    user: str
    password: str
    host: str


class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("List command has loaded successfully!")

    @commands.command()
    async def list(self, ctx):
        dotenv.load_dotenv()
        # NOTE: Using TypedDict to pass db params
        postgres = DataBaseConfig(
            os.getenv("database"),
            os.getenv("user"),
            os.getenv("password"),
            os.getenv("host"),
        )
        db_con = PostgresConnection(postgres)
        #
        # postgres = PostgresConnection(
        #     os.getenv("database"),
        #     os.getenv("user"),
        #     os.getenv("password"),
        #     os.getenv("host"),
        # )
        template = f"Claro, mestre {ctx.author}.\n Aqui esta a lista de nomes no meu banco de dados: \n"
        for row in db_con.getAllNames("user_table"):
            template += f"{row[1]}\n"
        await ctx.send(template)


async def setup(bot):
    await bot.add_cog(List(bot))
