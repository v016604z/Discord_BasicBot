from discord.ext import commands
import discord
import asyncio
import json
import random
import aiohttp
import io

with open("D:\work_space\Discord_BasicBot\setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():                               #bot啟動訊息
    print(f'We have logged in as {bot.user}')

@bot.event                                          
async def on_member_join(member):                   #成員進入
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}join!')

@bot.event
async def on_member_remove(member):                 #成員離開
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}leave!')

@bot.command()                                      #ping顯示
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)')

@bot.command()                                      #隨機本機照片
async def randomPicture(ctx):
    pic=discord.File(random.choice(jdata['pic']))
    await ctx.send(file=pic)

@bot.command()                                      #隨機網路照片
async def webPicture(ctx):
    await ctx.send(random.choice(jdata['url_pic']))

bot.run(jdata["TOKEN"])                             #bot執行