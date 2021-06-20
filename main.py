import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'L!')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Bủh bủh lmao'))
  print('Bot đã on.')
  
@client.event
async def on_member_join(member):
  print(f'{member} đã vào server.')
  
@client.event
async def on_member_remove(member):
  print(f'{member} đã rời server.')
  
@client.command()
async def ping(ctx):
  await ctx.send(f'Độ trễ của bot là {round(client.latency * 1000)} ms')
  
@client.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  
client.run('ODQzMDY5MzU4MTA3NjU2MjEz.YJ-fhg.XDGRErOKcm8a1eqshg88VYNaBoY')