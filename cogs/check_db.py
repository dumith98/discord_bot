import discord
from pg_queries import random_info
from discord.ext import commands

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
        await ctx.send(f'{random_info.CheckUser()}')

async def setup(bot):
    await bot.add_cog(List(bot))
