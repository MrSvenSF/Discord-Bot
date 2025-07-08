from discord.ext import commands

class AutoDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("AutoDelete Cog loaded successfully!")
    
    
def setup(bot):
    bot.add_cog(AutoDelete(bot)) 