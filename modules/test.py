import discord

def setup(bot: discord.Bot) -> None:

    @bot.slash_command(name="hello", description="Say hello to the bot")
    async def hello(ctx: discord.ApplicationContext):
        await ctx.respond("Hey!")


__all__ = ["setup"]