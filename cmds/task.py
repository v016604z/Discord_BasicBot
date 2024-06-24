import discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import json,asyncio,datetime,time

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class Task(Cog_Extension):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.interval.start()
        self.channel = None
        
    #設定發布時間
    @commands.command()
    async def set_time(self, ctx, *, time):
        with open("setting.json", 'r', encoding='utf-8') as jfile:
            jdata = json.load(jfile)
        jdata['Time'] = time
        with open("setting.json", 'w', encoding='utf-8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.channel.send("已設定時間")
        await self.start_task()
    
    async def start_task(self):
        now = datetime.datetime.now()
        dt = datetime.datetime.strptime(jdata['Time'], '%m/%d/%y %H:%M:%S')
        seconds_to_wait = (dt - now).total_seconds()
        if(seconds_to_wait > 0):
            print(seconds_to_wait)
            await asyncio.sleep(seconds_to_wait)
        await self.task()
    
    #鬧鐘
    async def task(self):
        await asyncio.sleep(1)
        self.channel = self.bot.get_channel(1157653005324255296)
        await self.channel.send("Hi, time over!")
    
    

async def setup(bot):
    await bot.add_cog(Task(bot))
    
    # def cog_unload(self):
    #     self.interval.cancel()

    # @tasks.loop(seconds=5)
    # async def interval(self):
    #     self.channel = self.bot.get_channel(1157653005324255296)
    #     if self.channel is not None:
    #         await self.channel.send("Hi, I'm running!")
    
    # @commands.command()
    # async def set_channel(self, ctx, ch: int):
    #     self.channel = self.bot.get_channel(ch)
    #     await ctx.send(f'Set Channel: {self.channel.mention} (ID: {self.channel.id})')

