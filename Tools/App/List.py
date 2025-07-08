from discord.ext import commands

class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("List Cog loaded successfully!")
    
    
def setup(bot):
    bot.add_cog(List(bot)) 