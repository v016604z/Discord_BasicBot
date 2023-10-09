import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
    
    @commands.command()                              #ping顯示
    async def ping(selF,ctx):
        await ctx.send(F'{round(selF.bot.latency*1000)}(ms)')

async def setup(bot):
    await bot.add_cog(Main(bot))