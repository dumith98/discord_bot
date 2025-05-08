import os
import discord
from discord.app_commands import command
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

def main():
    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

    async def Load():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

    async def main():
        async with bot:
            await Load()
            await bot.start(TOKEN)

    @bot.event
    async def on_ready():
        print(f'\n{bot.user.name} has connected successfully!')

#
# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f'Fala {member.name}!, Se esta lendo isso que dizer que deu bom!')
#
# @bot.command(name='ping')
# async def ping(ctx):
#     await ctx.send('pong')

    asyncio.run(main())


if __name__ == '__main__':
    main()
