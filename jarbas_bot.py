import os
import discord
from discord.app_commands import command
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


class JarbasClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to {discord.utils.get(self.guilds, name=GUILD)}')


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Fala {member.name}!, Se esta lendo isso que dizer que deu bom!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected successfully!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)

