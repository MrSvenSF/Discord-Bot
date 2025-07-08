from discord.ext import commands

GUILD_ID = 1388186263944691816

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Test Cog loaded successfully!")

    @commands.slash_command(description="Test", guild_ids=[GUILD_ID])
    async def test(self, ctx):
        await ctx.respond('Test!')

def setup(bot):
    bot.add_cog(Test(bot)) 