import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):
    @commands.command()                                      #隨機本機照片
    async def randomPicture(selF,ctx):
        pic=discord.File(random.choice(jdata['pic']))
        await ctx.send(file=pic)

    @commands.command()                                      #隨機網路照片
    async def webPicture(selF,ctx):
        await ctx.send(random.choice(jdata['url_pic']))

async def setup(bot):
    await bot.add_cog(React(bot))