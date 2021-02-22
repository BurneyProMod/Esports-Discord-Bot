import discord
from discord.ext import commands

class Esports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.teamName = 'None'
    
    #TODO: The message skips the '@everyone' role due to everyone getting pinged when it's called. Find a way to stop this message from doing so. 

    @commands.command(name='GetRoles', description='Returns the list of all roles in this server.')
    @commands.guild_only()
    async def GetRoles(self, ctx):
        # Make a variable for the string since ctx.send() can only accept 1 variable. 
        printList = ""
        # Iterate through guild.roles List
        for role in ctx.guild.roles[1:]:
            # Get the name of the Role in type string and add it to the printList string.
            printList += role.name
            # Seperate each role with a comma
            printList += ', '
        # Print the completed list.
        await ctx.send(printList)
        
def setup(bot):
    bot.add_cog(Esports(bot))