import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event                                          #成員進入
async def on_member_join(member):
    chanel=bot.get_channel(1157653005324255296)
    await chanel.send(F'{member}join!')
    

@bot.event
async def on_member_remove(member):                 #成員離開
    chanel=bot.get_channel(1157653005324255296)
    await chanel.send(F'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)')

bot.run('MTE1NzY0OTg0Nzg4NTc3MDg4Mw.GXiMPf.nfS20TtOvcMXItrNLwI5nFugtH5NuroBDUt2F4')