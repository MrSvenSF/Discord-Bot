from discord.ext import commands

class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("AntiSpam Cog loaded successfully!")
    
    
def setup(bot):
    bot.add_cog(AntiSpam(bot)) 