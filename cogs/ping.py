import discord
from discord.ext import commands
import structlog

logger = structlog.get_logger()


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Ping command has loaded successfully!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Ponging you Pong! \nYour name is: {ctx.author}")


async def setup(bot):
    await bot.add_cog(Ping(bot))
