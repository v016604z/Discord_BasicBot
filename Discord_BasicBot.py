import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    chanel=client.get_channel(1157653005324255296)
    await chanel.send(F'{member}join!')
    

@client.event
async def on_member_remove(member):
    chanel=client.get_channel(1157653005324255296)
    await chanel.send(F'{member}leave!')

client.run('MTE1NzY0OTg0Nzg4NTc3MDg4Mw.GXiMPf.nfS20TtOvcMXItrNLwI5nFugtH5NuroBDUt2F4')