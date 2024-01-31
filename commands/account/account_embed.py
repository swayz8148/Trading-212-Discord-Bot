import discord

def create_account_embed(data):
    """Create a portfolio embed from an item."""
    embed = discord.Embed(title="Account Information", color=0x3498db)
    
    for key, value in data.items():
        embed.add_field(name=key, value=value, inline=False)
    
    return embed