import os
from discord.ext import tasks
import requests
from .portfolio import create_portfolio_embed

LOOP_TIME = 20
PORTFOLIO_URL = "https://live.trading212.com/api/v0/equity/portfolio"
HEADERS = {"Authorization": os.getenv('AUTHORIZATION')}

@tasks.loop(minutes=LOOP_TIME)
async def portfolio(bot):
    channel = bot.get_channel(os.getenv('CHANNEL_ID'))
    data = requests.get(PORTFOLIO_URL, headers=HEADERS).json()
    for item in data:
        await channel.send(embed=create_portfolio_embed(item))