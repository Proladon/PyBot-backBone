import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Func, Logger
from core import check
import json
import os, random

class Main(Cog_Extension):

	'''
	等待使用者回覆檢查 (需要時複製使用)
	async def user_respone():
		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel
		respone = await self.bot.wait_for('message', check=check)
		return respone

	respone_msg = await user_respone
	'''

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.bot.latency*1000)} ms')

	@commands.command()
	@check.valid_user()
	async def test(self, ctx):
		await ctx.send('Bee! Bo!')


def setup(bot):
	bot.add_cog(Main(bot))