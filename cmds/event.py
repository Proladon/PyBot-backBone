import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.errors import Errors
import json, datetime, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Event(Cog_Extension):
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		'''指令錯誤觸發事件'''
		error_command = '{0}_error'.format(ctx.command)
		try:
			# 檢查是否有 Custom Error Handler
			if hasattr(Errors, error_command):
				await Errors.error_command()
				return
			# 使用 Default Error Handler
			else:
				await Errors.default_error(self, ctx, error)
		except AttributeError:
			pass

def setup(bot):
	bot.add_cog(Event(bot))