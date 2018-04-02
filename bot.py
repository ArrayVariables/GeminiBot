import os, re
try:
	import discord
	from discord import embeds
	from discord.ext import commands 
	from discord.ext.commands import Bot
	import random # It comes preloaded.
	import asyncio
	import aiohttp
	import bs4
	from bs4 import BeautifulSoup, BeautifulStoneSoup
	import pylint
	import chalk
except ImportError:
	print('''You haven't installed discord.py, or,
you might be using the outdated 0.16.12.
Rewrite : pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
Please note : This bot doesn't use or support music,
but if you wish so, modify the code.''')

class Bot():
	'''The core of the bot.
	I should say, this is too much of a work.
	'''
	
	def __init__(self, bot):
		self.bot = bot
		
	description = '''A bot I guess.'''
	bot = commands.Bot(command_prefix=';;', description=description)
		
	@bot.event
	async def on_ready():
		if bot.user.id == 383561620661731329:
			developer_mode = True as On
		else:
			developer_mode = False as Off
			
		print(f'{self.user.name}')
		print('Startup Screen')
		print('Version: 0.7.2')
		print(f'Bot ID: {self.user.id}')
		print(f'discord.py version: {discord.__version__}')
		print(f'Developer Mode : {developer_mode}')
		
	@bot.event
	async def on_command_error(ctx, error):
		if isinstance(error, commands.NotOwner):
			await ctx.send('The command is only accessed by the bot owner!')
		elif isinstance(error, commands.BadArgument):
			await ctx.send('Looks like I cannot find that user.')
			
	@bot.command()
	async def ping(ctx):
		pingMSG = 'Pong!'
		await ctx.send(pingMSG)
    
# Upgrading GeminiBot to a next level.
