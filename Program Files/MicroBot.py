import discord
from discord.ext import commands
import random

description = '''A bot to defeat all other bots.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def multiply(left : int, right : int):
	"""Multiplies two numbers together"""
	await bot.say(left * right)

@bot.command()
async def divide(left : int, right : int):
	"""Divides two numbers"""
	await bot.say(left / right)

@bot.command()
async def subtract(left : int, right : int):
	"""Subtracts two numbers"""
	await bot.say(left - right)
	
@bot.command(pass_context=True)
async def tell(ctx, name : str):
	"""Tells the user to get in discord"""
	server = ctx.message.server
	my_member = server.get_member_named(name)	
	await bot.say(my_member.mention)
	await bot.say("GET IN DISCORD!!!!!!!")

bot.run('Enter Token Here')
