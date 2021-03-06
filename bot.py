import os
import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"), description='Algobot', intents=intents)
bot.remove_command('help')

if __name__ == '__main__':
	for cog in os.listdir(os.getcwd()+"/cogs"):
		if cog[-3:len(cog)] == '.py':
			bot.load_extension('cogs.'+cog[:-3])

@bot.event
async def on_ready():
	print("Logged in as: "+str(bot.user)+"\nVersion: "+str(discord.__version__))

token_file = open("auth/token.dat", "r").read()
bot.run(token_file, bot=True, reconnect=True)
