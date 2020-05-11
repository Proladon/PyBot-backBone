import discord
from discord.ext import commands
from core.classes import Cog_Extension, Logger
from cmds.main import Main #導入 Main Cog
import json, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Errors():
	# 自訂 Error Handler
	
	@Main.sayd.error
	'''Main.sayd 指令錯誤處理'''
	async def sayd_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('請輸入要覆誦的訊息')
			Logger.log(self, ctx, error)
			
		


	# 預設 Error Handler
	async def default_error(self, ctx, error):
		# default_check = False
		if isinstance(error, commands.MissingRequiredArgument):
			# default_check = True
			await ctx.send(self, error)
			Logger.log(self, ctx, error)
		else:
			await ctx.send(f'未知錯誤: {error}')
			Logger.log(self, ctx, error)
