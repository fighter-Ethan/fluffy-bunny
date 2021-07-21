#Imports
import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
import asyncio
from webserver import keep_alive
import os
import json
import requests
import random

#Commands Handler- DO NOT TOUCH
client = commands.Bot(command_prefix="fb!" , case_insensitive = True)
member = discord.Member

#Removes the default help command.
client.remove_command('help')

#Matrix
robot= ["Rock" , "Paper" , "Scissors"]

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "Fluffy Bunny in " +  str(len(client.guilds)) + " servers | fb!help"))
  print('Bot is ready!')

@client.command()
async def help(ctx):
  embed = discord.Embed(title = "**Help Menu**" , description = "*Fluffy Bunny!*" , color = discord.Color.green())
  embed.add_field(name = "**play [value]**" , value = "The main command. Used to play the game!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**invite**" , value = "Invites the bot to your server!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**support**" , value = "Invites you to the support server!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**ping**" , value = "Shows the ping, in ms, of the bot! Bunny go brrr" + "\n\u200b" , inline = True)
  embed.set_thumbnail(url = "https://tse3.mm.bing.net/th?id=OIP.gvF01vMVxN8H95xkHHMW0AHaEK&pid=Api&P=0&w=302&h=171")
  embed.set_footer(text = "Make sure to give Fluffy Bunny plenty of carrots!")
  await ctx.send(embed=embed)

@client.command()
async def play(ctx, choice = "Null"):
  rrobot = random.choice(robot)
  if choice == "Null":
    await ctx.send("No fair! Choose something!")
  elif choice == "Rock":
    if rrobot == "Rock":
      await ctx.send("I choose... **rock!**")
      await asyncio.sleep(1)
      await ctx.send("Darn! It was a tie!")
    if rrobot == "Paper":
      await ctx.send("I choose... **paper!**")
      await asyncio.sleep(1)
      await ctx.send("Hah! I win!")
    if rrobot == "Scissors":
      await ctx.send("I choose... **scissors!**")
      await asyncio.sleep(1)
      await ctx.send("Darn it... you won!")
  elif choice == "Paper":
    if rrobot == "Rock":
      await ctx.send("I choose... **rock!**")
      await asyncio.sleep(1)
      await ctx.send("Darn it... you won!")
    if rrobot == "Paper":
      await ctx.send("I choose... **paper!**")
      await asyncio.sleep(1)
      await ctx.send("Darn! It was a tie!")
    if rrobot == "Scissors":
      await ctx.send("I choose... **scissors!**")
      await asyncio.sleep(1)
      await ctx.send("Hah! I win!")
  elif choice == "Scissors":
    if rrobot == "Rock":
      await ctx.send("I choose... **rock!**")
      await asyncio.sleep(1)
      await ctx.send("Hah! I win!")
    if rrobot == "Paper":
      await ctx.send("I choose... **paper!**")
      await asyncio.sleep(1)
      await ctx.send("Darn it... you won!")
    if rrobot == "Scissors":
      await ctx.send("I choose... **scissors!**")
      await asyncio.sleep(1)
      await ctx.send("Darn! It was a tie!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000 , 0)) + "ms")

@client.command()
async def support(ctx):
  await ctx.send("https://discord.gg/VtfUCjejXq")
  
@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=867279928948162560&permissions=122048&scope=bot")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
