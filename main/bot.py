# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='>')

@bot.command(name='Elder', help='Responds with a random quote from The Elder Scrolls')
async def elderScrollsDialogue(ctx):
    elderQuotes = [
        'I was born 87 years ago. For 65 years I\'ve ruled as Tamriel\'s Emperor. But for all these years, I\'ve never been the ruler of my own dreams. I have seen the Gates of Oblivion, beyond which no waking eye may see. Behold, in darkness a doom sweeps the land. This is the 27th of Last Seed, the year of Akatosh, 433. These are the closing days of the 3rd Era...and the final hours of my life',
        'Lord Dagon will welcome your soul in Oblivion!',
        'You sleep rather soundly for a murderer. That\'s good. You\'ll need a clear conscience for what I\'m about to propose.',
        'I see you are a follower of the Gray Fox',
        'I saw a mudcrab the other day, horrible little creatures',
        'THIS IS THE PART WHERE YOU FALL DOWN AND BLEED TO DEATH',
    ]

    response = random.choice(elderQuotes)
    await ctx.send(response)

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


bot.run(TOKEN)