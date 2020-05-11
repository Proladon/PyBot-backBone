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
		'''Bot 延遲'''
		await ctx.send(f'{round(self.bot.latency*1000)} ms')

	@commands.command()
	@check.valid_user() #檢查權限, 是否存在於效人員清單中, 否則無法使用指令
	async def test(self, ctx):
		'''有效人員 指令權限測試'''
		await ctx.send('Bee! Bo!')
		
	@commands.command()
	async def sayd(self, ctx, *content: str):
		'''訊息覆誦'''
		await ctx.send(content)


def setup(bot):
	bot.add_cog(Main(bot))
