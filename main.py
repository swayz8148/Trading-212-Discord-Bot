import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from commands.portfolio.portfolio import create_portfolio_embed
from commands.portfolio.portfolio_loop import portfolio
from commands.portfolio.send_portfolio import send_portfolio
from commands.portfolio.set_interval import set_interval, start_portfolio, stop_portfolio
from commands.help.help_command import help
from commands.account.account import send_account

load_dotenv()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot.remove_command('help')
bot.add_command(help)
bot.add_command(set_interval)
bot.add_command(start_portfolio)
bot.add_command(stop_portfolio)
bot.add_command(send_portfolio)
bot.add_command(send_account)

@bot.event
async def on_ready():
    guild_id = int(os.getenv('GUILD_ID'))
    guild = bot.get_guild(guild_id)
    portfolio.start(guild, bot)

bot.run(os.getenv('BOT_TOKEN'))