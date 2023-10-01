from discord.ext import commands
from core.classes import Cog_Extension
import discord

class Main(Cog_Extension):
    
    @commands.command()                              #ping顯示
    async def ping(selF,ctx):
        await ctx.send(F'{round(selF.bot.latency*1000)}(ms)')
    
    @commands.command()                              #ping顯示
    async def hi(selF,ctx):
        await ctx.send(F'abc1')

async def setup(bot):
    await bot.add_cog(Main(bot))