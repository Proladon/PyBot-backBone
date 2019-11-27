import discord
from discord.ext import commands
import json

def valid_user():
	'''有效人員檢查器'''
	def predicate(ctx):
		with open('setting.json', 'r', encoding='utf8') as jfile:
		   jdata = json.load(jfile)
		return ctx.message.author.id == jdata['Owner_id'] or ctx.message.author.id in jdata['Valid_User']
	return commands.check(predicate)