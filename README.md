
# Discord Server Metrics Bot

A Discord bot built with `discord.py` that captures server metrics, stores them
in an SQLite database, and presents them via a Flask web application.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
  - [Bot Permissions](#bot-permissions)
  - [Inviting the Bot](#inviting-the-bot)
- [Running the Bot and Web Application](#running-the-bot-and-web-application)
- [Contributing](#contributing)
- [License](#license)

## Features

- Capture real-time server metrics from Discord.
- Store metrics in an SQLite database.
- Display metrics via a Flask web application.

## Prerequisites

- Python 3.6+
- Pip package manager
- A Discord account and server with administrative access

## Setup

### Environment Variables

1. Create a `.env` file in the root of your project directory.
2. Add your bot token to the `.env` file:

``` DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN ```

### Database Setup

1. Run the `database_setup.py` script to initialize the SQLite database:

```bash python database_setup.py ```

### Bot Permissions

Ensure your bot has the following permissions:

- Read Messages
- Send Messages
- View Audit Log
- (Any other permissions required by your bot's functionality)

### Inviting the Bot

1. Go to the [Discord Developer
Portal](https://discord.com/developers/applications).
2. Click on your bot application.
3. Navigate to the "OAuth2" section.
4. Under "OAuth2 URL Generator", select "bot" in the "SCOPES" section.
5. Select the necessary permissions in the "BOT PERMISSIONS" section.
6. Copy the generated URL, open it in your browser, select a server, and invite
your bot.

## Running the Bot and Web Application

1. Start the bot:

```bash python discord_bot.py ```

2. In a separate terminal, start the Flask application:

```bash python app.py ```

3. Open a web browser and navigate to `http://localhost:5000/metrics` to view
the metrics.

## Contributing

Contributions are welcome! Please fork this repository and open a pull request
with your changes.

## License

[MIT License](LICENSE.md)
