
import discord
from discord.ext import commands
from discord import utils


client = commands.Bot(command_prefix='why') # why


curseWord = [
    '🏃🏿', '🦼', '🧑🏿‍🦼', '🧍🏿', 'дудка', 'dudka',
    'дудец', '🏳️‍🌈'] 
@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, sorry but its not allowed here aaaaa") # text, when bot removes a word
    else:
        return



@client.event
async def on_raw_reaction_add(payload):
    channelid = payload.channel_id
    user = payload.member
    messageid = payload.message_id
    if channelid == 9339: # type ur channel id
        channel = bot.get_channel(channelid)
        message = await channel.fetch_message(messageid)
        for reaction in message.reactions:
            await reaction.remove(user) # reaction remove (too lazy to make normal)
    else:
        return

@client.event
async def on_ready():
    print("Online")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Deleting Some dudkas...")) # status




client.run('your token') # token

