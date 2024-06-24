import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    
    @commands.command()                              #ping顯示
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')
        
    @commands.command()                              #清除字數
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num + 1)

        
async def setup(bot):
    await bot.add_cog(Main(bot))



