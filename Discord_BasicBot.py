import discord
from discord.ext import commands
import json

with open("D:\work_space\Discord_BasicBot\setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():                               #bot啟動訊息
    print(f'We have logged in as {bot.user}')

@bot.event                                          #成員進入
async def on_member_join(member):
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}join!')
    

@bot.event
async def on_member_remove(member):                 #成員離開
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}leave!')

@bot.command()                                      #ping顯示
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)')

bot.run(jdata["TOKEN"])                             #bot執行