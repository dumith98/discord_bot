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

client = JarbasClient(intents=discord.Intents.all())

@client.event
async def on_member_join(member):
    await member.create.dm()
    await member.dm_channel.send(f'Fala {member.name}!, Se esta lendo isso que dizer que deu bom!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong')



# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @bot.command(name='ping')
# async def ping(ctx):
#     await ctx.send('pong')

# @bot.event
# async def on_message(message):
    

# bot.run(TOKEN)

client.run(TOKEN)
