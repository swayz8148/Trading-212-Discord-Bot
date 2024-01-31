import os
from discord.ext import tasks
from discord.utils import get
import requests
from .portfolio import create_portfolio_embed

LOOP_TIME = 60
PORTFOLIO_URL = "https://live.trading212.com/api/v0/equity/portfolio"
HEADERS = {"Authorization": os.getenv('AUTHORIZATION')}

@tasks.loop(minutes=LOOP_TIME)
async def portfolio(bot, ctx):
    channel = get(ctx.guild.channels, name='trading')
    data = requests.get(PORTFOLIO_URL, headers=HEADERS).json()
    for item in data:
        await channel.send(embed=create_portfolio_embed(item))