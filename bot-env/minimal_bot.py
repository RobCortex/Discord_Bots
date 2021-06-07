import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('How are you?'):
        await message.channel.send('Fine!')

    if message.content.startswith('That is all for now.'):
        await client.close()

client.run('ODUxMjUxODg2Mzc4OTc1Mjgz.YL1kGQ.YvI5AXuEr41LIKKmRrBk2ToIE-o')
