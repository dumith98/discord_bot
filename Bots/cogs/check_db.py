# import discord
from ../pg_queries.random_info import CheckUser
from discord.ext import commands

class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("List command has loaded successfully!")

    @commands.command()
    async def list(self, ctx):
        await ctx.send(CheckUser())

async def setup(bot):
    await bot.add_cog(List(bot))
