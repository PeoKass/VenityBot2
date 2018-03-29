import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.startswith('!ip'):
       userID = message.author.id
       await client.send_message(message.channel, "<@{}> Meie Venity serveri ip on: 37.187.156.107:25664 !".format(userID))

       
@client.event
async def on_message(message):
    if message.content.startswith('!meeskond'):
       userID = message.author.id
       await client.send_message(message.channel, "<@{}> Omanik:PeoKass           Omanik:DontTryMeee              Abi-Omanik:RobRun".format(userID))


       
client.run("NDI4OTI0NzIwNzYzNjMzNjc0.DZ64Xg.KUPunPRBANZD4t2O1TLHBhCL-Vc")
