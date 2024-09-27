import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import app_commands

class Main(Cog_Extension):
    
<<<<<<< Updated upstream
    @commands.command()                              #ping顯示
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')
        
    @commands.command()                              #清除字數
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num + 1)
=======
    @app_commands.command(name = "ping", description = "Show ping!")    #ping顯示
    async def ping(selF,interaction: discord.Interaction):
        await interaction.response.send_message(F'{round(selF.bot.latency*1000)}(ms)')

    @app_commands.command(name='hello', help='Greets the user!')  
    async def hello(ctx):
        await ctx.send("Hello World!")
>>>>>>> Stashed changes

        
async def setup(bot):
    await bot.add_cog(Main(bot))



