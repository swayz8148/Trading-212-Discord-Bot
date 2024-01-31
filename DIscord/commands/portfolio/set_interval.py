from discord.ext import commands
from commands.portfolio.portfolio_loop import portfolio

@commands.command()
@commands.has_permissions(administrator=True)
async def set_interval(ctx, minutes: int):
    global LOOP_TIME
    LOOP_TIME = minutes
    portfolio.change_interval(minutes=minutes)
    await ctx.send(f'Interval set to {minutes} minutes.')
    await ctx.message.delete()

@commands.command()
@commands.has_permissions(administrator=True)
async def start_portfolio(ctx):
    portfolio.start(ctx.bot)
    await ctx.send('Portfolio loop started.')

@commands.command()
@commands.has_permissions(administrator=True)
async def stop_portfolio(ctx):
    portfolio.stop()
    await ctx.send('Portfolio loop stopped.')