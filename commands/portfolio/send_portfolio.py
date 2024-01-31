import os
from discord.ext import commands
import requests
from .portfolio import create_portfolio_embed

PORTFOLIO_URL = "https://live.trading212.com/api/v0/equity/portfolio"
HEADERS = {"Authorization": os.getenv('AUTHORIZATION')}

@commands.command()
@commands.has_permissions(administrator=True)
async def send_portfolio(ctx):
    channel = ctx.channel
    response = requests.get(PORTFOLIO_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            await channel.send(embed=create_portfolio_embed(item))
    else:
        print(f"Error: Received status code {response.status_code} from server")