import discord

def create_portfolio_embed(item):
    """Create a portfolio embed from an item."""
    profit = (item['currentPrice'] - item['averagePrice']) * item['quantity']
    emoji = '📈' if profit >= 0 else '📉'
    profit_str = f"**{emoji} {profit:.2f}**"
    value_in_pounds = item['quantity'] * item['currentPrice']
    value_str = f"£{value_in_pounds:.2f}"
    embed = discord.Embed(title=item['ticker'], color=discord.Color.blue())
    embed.add_field(name="Quantity", value=item['quantity'], inline=True)
    embed.add_field(name="Value in £", value=value_str, inline=True)
    average_price = round(item['averagePrice'], 2)
    average_price_str = f"£{average_price:.2f}"
    embed.add_field(name="Average Price", value=average_price_str, inline=True)
    current_price = round(item['currentPrice'], 3)
    current_price_str = f"£{current_price:.2f}"
    embed.add_field(name="Current Price", value=current_price_str, inline=True)
    embed.add_field(name="Profit", value=profit_str, inline=True)
    return embed