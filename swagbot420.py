import discord
import random

text = ['fuck you','retard','shut up','ur parents dont love u','why do u bother living','u have no friends','suck a dick','https://logal.media/vnULVo_IsK.gif','ur whole family is dissapointed in u','u have more fingers than iq','stupid bitch','ok airplane','ur ancestry incestry','https://logal.media/aHrVwW1YQ.jpg']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(client.user.mention)

    if client.user in message.mentions:
        await message.channel.send(random.choice(text))

client.run('bot token here')