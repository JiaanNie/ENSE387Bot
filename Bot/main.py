import discord
import serial

#
# #TOKEN = 'NTI1OTI4NDM4Mzk0MjU3NDA4.DwG4VQ.s_CfQVl7F5LhFk7y3G1NGvAzr0g'
#TOKEN = "NTI3MzI1ODMxODIzODg0MzI4.DwSGzg.1874KiUFa3PXPoYWtJJHyGM2eTY"
TOKEN = "NTYxNjk3MDAzMzI3NzE3NDAz.XKABSQ.2eVUPIpS-Ft4wKsqgVONJw0_LAI"
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!purpose'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!up'):
        msg = "Moving the bot up by 3 second".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!down'):
        msg = "Moving the bot down by 3 second".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!right'):
        msg = "Moving the bot right by 3 second".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!left'):
        msg = "Moving the bot left by 3 second".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
