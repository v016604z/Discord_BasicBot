import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from pytube import YouTube

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    
    #成員進入
    @commands.Cog.listener()
    async def on_member_join(self,member):                   
        chanel=self.bot.get_channel(int(jdata["Channel"]))
        await chanel.send(F'{member}join!')

    #成員離開
    @commands.Cog.listener()
    async def on_member_remove(self,member):                 
        chanel=self.bot.get_channel(int(jdata["Channel"]))
        await chanel.send(F'{member}leave!')
    
    #YT下載
    @commands.Cog.listener()
    async def on_message(self,meg):
        if meg.author == self.bot.user:
            return
        with open('data\\user_data.json') as f:
            user = json.load(f)
        if str(meg.author) == user["User_id"]:
            print("download...")
            YT = YouTube(str(meg.content))
            video = YT.streams.filter().get_highest_resolution().download()
            print("download finish")
            with open(video, 'rb') as f:
                picture = discord.File(f)
                await meg.channel.send(file=discord.File(stream.download))
        if meg.content.startswith("!download"):
            await meg.channel.send("Please Type the Link")
            jsonFile = open('data\\user_data.json','w')
            data = {}
            data["User_id"] = f'{meg.author}'
            jsonFile.write(json.dumps(data))        # 寫入資料
            jsonFile.close()
        
                
async def setup(bot):
    await bot.add_cog(Event(bot))
    