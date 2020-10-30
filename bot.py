import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

# For discord.py 1.5 breaking changes
# Please read the offical API doc:
# https://discordpy.readthedocs.io/en/latest/intents.html#intents-primer
intents = discord.Intents.all()

# load settings
with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

bot = commands.Bot(command_prefix=jdata['Prefix'], owner_ids=jdata['Owner_id'])

@bot.event
async def on_ready():
	print(">> Bot is online <<")

# load all extensions
for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(jdata['TOKEN'])
	
