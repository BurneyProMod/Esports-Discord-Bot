import discord
import datetime
from discord.ext import commands


class Esports(commands.Cog):

    #Dictionaries to help with input validation
    #TODO: There has got to be a better way to do this. 
    timeofday = ['12:00am', '1:00am', '2:00am', '3:00am', '4:00am', '5:00am', '6:00am', '7:00am', '8:00am', '9:00am', '10:00am', '11:00am', '12:00pm', '1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm', '12:00pm']

    def __init__(self, bot):
        self.bot = bot
        self.teamName = 'None'
        self.practiceSchedule = []

    #TODO: The message skips the '@everyone' role due to everyone getting pinged when it's called. Find a way to stop this message from doing so. 

    @commands.command(name='Getroles', help='Returns the list of all roles in this server.')
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

    @commands.command(name='teamname', help='Lets the bot know which server role the team is assigned.')
    @commands.guild_only()
    async def TeamName(self, ctx, arg: discord.Role):
        try:
            index = ctx.guild.roles.index(arg)
            self.teamName = ctx.guild.roles[index]
            await ctx.send('Teamname has been successfully set!')
        except:
            # TODO: Figure out how to do this exception:
            # discord.ext.commands.errors.RoleNotFound: Role "blah" not found.
            print()

    @commands.command(name='check', help='Sends a message of the currently active Team Name')
    @commands.guild_only()
    async def check(self, ctx):
        if(self.teamName == 'None'):
            await ctx.send("There is no Team Name set. Set one with the >teamname command!")
        else:
            str = 'The current teamname is' + self.TeamName
            await ctx.send(str)

    @commands.command(name='practice', help='Sets a practice time. Format: >practice dd/mm/yy 00:00am')
    @commands.guild_only()
    async def Practice(self, ctx, practiceDay, practiceTime: str):
        if (self.teamName == 'None'):
            await ctx.send('A Team has not been assigned. Please use the >Teamname command to set one.')
        else:
            day,month,year = practiceDay.split('/')
            try:
                datetime.datetime(int(year),int(month),int(day))    
                if(practiceTime in self.timeofday):
                    self.practiceSchedule.append(practiceDay + ' at ' + practiceTime)
                    await ctx.send('Schedule successfully updated!')
            except ValueError:
                print("practice Date: " + day + ' ' + month + ' ' + year)
                print("Pracitce Time: " + practiceTime)
                await ctx.send('The day entered is incorrect. Please check the format by typing >help')

    @commands.command(name='getsched', help='Sends the user the current schedule of practices')
    @commands.guild_only()
    async def getsched(self, ctx):
        if not self.practiceSchedule:
            await ctx.send("Nothing currently scheduled.")
        else:
            str = ""
            for i in self.practiceSchedule:
                str += i
                str += '\n'
            await ctx.send(str)

def setup(bot):
    bot.add_cog(Esports(bot))