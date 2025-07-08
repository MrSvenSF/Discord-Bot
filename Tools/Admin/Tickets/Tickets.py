from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Tickets Cog loaded successfully!")
    
    
def setup(bot):
    bot.add_cog(Tickets(bot)) 