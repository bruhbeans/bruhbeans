import os
from discord.ext import commands

bot = commands.Bot(command_prefix='-', help_command=None)

@bot.event
async def on_ready():
    print('login')

bot.run(os.getenv('TOKEN'))
