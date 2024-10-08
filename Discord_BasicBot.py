import discord
from discord.ext import commands
import json
import os
import asyncio

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#bot啟動訊息
@bot.event
async def on_ready():                               
    print(f'We have logged in as {bot.user}')

#成員進入
@bot.event                                          
async def on_member_join(member):                   
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}join!')

#成員離開
@bot.event
async def on_member_remove(member):                 
    chanel=bot.get_channel(int(jdata["Channel"]))
    await chanel.send(F'{member}leave!')

#載入類別
@bot.command()
async def load(ctx,extension):                      
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

#卸載類別
@bot.command()
async def unload(ctx,extension):                    
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

#重整類別
@bot.command()
async def reload(ctx,extension):                    
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

#類別自動匯入
async def load_extensions():
    for filename in os.listdir("cmds"):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

#執行load_extensions and bot執行
async def main():
    await load_extensions()                         
    await bot.start(jdata["TOKEN"])                 

if __name__ == '__main__':
    asyncio.run(main())