import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Func
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Mod(Cog_Extension):
	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="About P_Base-Bot", description="Made Bot Easier !", color=0x28ddb0)
		# embed.set_thumbnail(url="#")
		embed.add_field(name="開發者 Developers", value="Proladon#7525 (<@!149772971555160064>)", inline=False)
		embed.add_field(name="源碼 Source", value="[Link](https://github.com/Proladon/Proladon-DC_BaseBot)", inline=True)
		embed.add_field(name="協助 Support Server", value="[Link](https://discord.gg/R75DXHH)" , inline=True)
		embed.add_field(name="版本 Version", value="0.1.0 a", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
		embed.set_footer(text="Made with ❤")
		await ctx.send(embed=embed)
def setup(bot):
   bot.add_cog(Mod(bot))