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

@bot.command()
async def load(ctx,extension):                      #載入類別
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):                    #卸載類別
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx,extension):                    #重整類別
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

async def load_extensions():
    for filename in os.listdir("cmds"):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

async def main():
    await load_extensions()                         #執行load_extensions
    await bot.start(jdata["TOKEN"])                 #bot執行

if __name__ == '__main__':
    asyncio.run(main())