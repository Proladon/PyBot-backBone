import discord
from discord.ext import commands
import json

def valid_user():
	'''
	有效人員檢查器
	讀取json檔裡的 Owner_id 和 Valid_User，比對當前觸發指令的使用者是否符合以上兩者之一
	回傳比對結果, 兩者皆不符合False, 符合其中一者True
	'''
	def predicate(ctx):
		with open('setting.json', 'r', encoding='utf8') as jfile:
		   jdata = json.load(jfile)

		return ctx.message.author.id == jdata['Owner_id'] or ctx.message.author.id in jdata['Valid_User']

	return commands.check(predicate) 