import discord

def create_account_embed(item):
    """Create a portfolio embed from an item."""
    cash = item['cash']
    return discord.Embed(title="Account", color=discord.Color.blue()).add_field(name="Cash", value=f"£{cash:.2f}", inline=True)