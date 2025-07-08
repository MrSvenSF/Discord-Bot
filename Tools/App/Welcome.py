from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Welcome Cog loaded successfully!")


def setup(bot):
    bot.add_cog(Welcome(bot)) 