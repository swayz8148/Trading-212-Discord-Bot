from discord import Embed
from discord.ext import commands#

@commands.command()
async def help(ctx):
    embed = Embed(title="Help", description="List of commands are:", color=0x00ff00)
    embed.add_field(name="!help", value="Shows this message", inline=False)
    embed.add_field(name="!portfolio", value="Shows your portfolio", inline=False)
    embed.add_field(name="!set_interval", value="Sets the interval for the portfolio loop", inline=False)
    embed.add_field(name="!start_portfolio", value="Starts the portfolio loop", inline=False)
    embed.add_field(name="!stop_portfolio", value="Stops the portfolio loop", inline=False)
    embed.add_field(name="!send_account", value="Sends info about your account", inline=False)
    await ctx.send(embed=embed)