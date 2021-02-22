import discord
import os

from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = Bot(command_prefix='$')

#This is basiaclly a dot path import. 
initial_extensions = ['cogs.commands'] 

bot = commands.Bot(command_prefix='>', description='A bot to help schedule your team\'s practices and matches.')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    """https://github.com/BurneyProMod/Esports-Discord-Bot"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Connection Successful')
    await bot.change_presence(activity=discord.Game(name="Shopping for Keyboards"))

bot.run(TOKEN)