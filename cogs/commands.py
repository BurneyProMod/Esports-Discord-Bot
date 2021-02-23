import discord
import datetime

from discord.ext import commands, tasks

class Esports(commands.Cog):

    client = discord.Client()

    #Dictionaries to help with input validation
    #TODO: There has got to be a better way to do this. 
    timeofday = ['12:00am', '1:00am', '2:00am', '3:00am', '4:00am', '5:00am', '6:00am', '7:00am', '8:00am', '9:00am', '10:00am', '11:00am', '12:00pm', '1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm', '12:00pm']

    def __init__(self, bot):
        self.bot = bot
        self.teamName = 'None'
        self.practiceSchedule = []
        self.notifyUsers = []

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
            printString = 'The current teamname is' + self.TeamName
            await ctx.send(printString)

    @commands.command(name='practice', help='Sets a practice time. Format: >practice mm/dd/yy 00:00am')
    @commands.guild_only()
    async def Practice(self, ctx, practiceDay, practiceTime: str):
        if (self.teamName == 'None'):
            await ctx.send('A Team has not been assigned. Please use the >Teamname command to set one.')
        else:
            month,day,year = practiceDay.split('/')
            try:
                datetime.datetime(int(year),int(month),int(day))    
                if(practiceTime in self.timeofday):
                    self.practiceSchedule.append(practiceDay + ' at ' + practiceTime)
                    self.practiceSchedule.sort()
                    printString = 'New practice time set ' + practiceDay + ' at ' + practiceTime
                    await ctx.send(printString)
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
            printString = ""
            for i in self.practiceSchedule:
                printString += i
                printString += '\n'
            await ctx.send(printString)

    @commands.command(name='notifyme', help='The bot will ping whoever uses this command X hours before the next scheduled event. Format: >!notifyme xx')
    @commands.guild_only()
    async def notifyme(self, ctx):
        senderID = ctx.author.id
        try:
            if senderID in self.notifyUsers:
                await ctx.send("You are already in the ping group")
            self.notifyUsers.append(senderID)
            print("User successfully added to ping group")
            await ctx.send("Successfully added to ping group. Use command >unnotify to stop")
        except KeyError:
            print("KeyError for notify command")

    @commands.command(name='unnotifyme', help='The bot will no longer ping you reminders for practice')
    @commands.guild_only()
    async def unnotifyme(self, ctx):
        senderID = ctx.author.id
        try:
            if senderID not in self.notifyUsers:
                await ctx.send("You are not in the ping group")
            self.notifyUsers.remove(senderID)
            await ctx.send("Successfully removed from ping group")
        except KeyError:
            print("KeyError for unnotify command")

    @commands.command(name='notifylist', help='Prints list of users that have reminders enabled for the schedule')
    @commands.guild_only()
    async def notifylist(self, ctx):
        print("Current List: ")
        for x in range(len(self.notifyUsers)): 
            print(self.notifyUsers[x])
        print()
        if not self.notifyUsers:
            await ctx.send("The notify list is empty.")
            return
        printString = ""
        for i in self.notifyUsers:
            # TODO: I can't convert the id to a string username without mentioning all the users. Please send help. 
            print("Current list element is " + str(i))
            user = discord.Object(int(i))
            print("user = discord.Object(int(i)): " + str(user))
            user.display_name = f"<@{user.id}>"
            print("user.display_name = " + str(user.display_name))
            printString += str(user.display_name)
            print("printString updated")
            printString += '\n'
        printString = discord.utils.escape_mentions(printString)
        await ctx.send(printString)

def setup(bot):
    bot.add_cog(Esports(bot))