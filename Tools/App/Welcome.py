from discord.ext import commands

GUILD_ID = 1388186263944691816 # Ersetze dies mit deiner Server-ID, z.B. 123456789012345678

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Hallo", guild_ids=[GUILD_ID])
    async def Hallo(self, ctx):
        await ctx.respond('Hallo!')

def setup(bot):
    bot.add_cog(Welcome(bot)) 