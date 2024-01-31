import os
from discord.ext import commands
import requests
from .account_embed import create_account_embed

URL = "https://live.trading212.com/api/v0/equity/account/cash"
HEADERS = {"Authorization": os.getenv('AUTHORIZATION')}
# HEADERS = {"Authorization": "30626754ZIHAnjoJRqxxVkmwiWZcBeHgKNPiT"}

@commands.command()
@commands.has_permissions(administrator=True)
async def send_account(ctx):
    channel = ctx.channel
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        await channel.send(embed=create_account_embed(data))
    else:
        print(f"Error: Received status code {response.status_code} from server")