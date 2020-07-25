import discord
from discord.ext import commands
from core.classes import Cog_Extension, Global_Func
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Mod(Cog_Extension):

    @commands.command(aliases=['cc'])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, num: int, reason=None):
        '''清理指定數量訊息'''
        await ctx.channel.purge(limit=num + 1)
        
        levels = {
            "a": "非對應頻道內容",
            "b": "不雅用詞"
        }

        if reason is not None:
            if reason in levels.keys():
                await ctx.send(Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {levels[reason]}'))
        else:
            await ctx.send(content=Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {reason}'), delete_after=5.0)


def setup(bot):
   bot.add_cog(Mod(bot))