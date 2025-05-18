import discord
import os
from DatabaseConnections.PostgresConnection import PostgresConnection
from discord.ext import commands
import dotenv
import structlog

logger = structlog.get_logger()


class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Add command has loaded successfully!")

    @commands.command()
    async def add(self, ctx):
        dotenv.load_dotenv()
        postgres = PostgresConnection(
            os.getenv("database"),
            os.getenv("user"),
            os.getenv("password"),
            os.getenv("host"),
        )
        await ctx.send(
            f"Would you like me to add you to my database, lorde {ctx.author}?"
            "\n Yes or No?"
        )
        response = await self.bot.wait_for("message")
        if response.content.lower() == "no":
            ctx.send("Understood. I'll not add you to m database.")

        elif response.content.lower() == "yes":
            await ctx.send(
                f"Very well. Would you like your username, {ctx.author}, "
                "or your name to be added?"
                "\n Username or name? "
            )
            response = await self.bot.wait_for("message")
            if (
                response.content.lower() == "user"
                or response.content.lower() == "username"
            ):
                try:
                    await ctx.send(f"Marvelous! I'll add {ctx.author} to my database!")
                    await postgres.insertName("user_table", str(ctx.author))
                    logger.info("Name added to Database")
                except:
                    logger.warn("Failed to add name to database")


# NOTE: Place holder for interactive code
# @commands.command()
# async def game(self, ctx):
#     number = random.randint(0, 100)
#     for i in range(0, 5):
#         await ctx.send('guess')
#         response = await self.bot.wait_for('message')
#         guess = int(response.content)
#         if guess > number:
#             await ctx.send('bigger')
#         elif guess < number:
#             await ctx.send('smaller')
#         else:
#             await ctx.send('yes!')


async def setup(bot):
    await bot.add_cog(Add(bot))
