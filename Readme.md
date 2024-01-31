# Discord Bot

This is a Discord bot built with discord.py. It includes several commands for Trading 212 API. (This is my very first discord bot and i will be playing around with this to learn new stuff as i go)

## Commands

- `!set_interval <minutes>`: Sets the interval for the portfolio loop.
- `!start_portfolio`: Starts the portfolio loop.
- `!stop_portfolio`: Stops the portfolio loop.
- `!send_portfolio`: Sends the portfolio.
- `!send_account`: Sends info about your account

## Setup

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Set up your environment variables in a `.env` file. You'll need to set `BOT_TOKEN`, `AUTHORIZATION`, and `CHANNEL_ID`.
4. Run the bot with `python main.py`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
