import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'L!')

@client.event
async def on_ready():
  print('Bot đã on.')
  
client.run('ODQzMDY5MzU4MTA3NjU2MjEz.YJ-fhg.XDGRErOKcm8a1eqshg88VYNaBoY')