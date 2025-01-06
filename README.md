# WeatherBot

A lightweight IRC bot that provides real-time weather information using the Open-Meteo API. WeatherBot is designed to be simple to set up, easy to configure, and free to use as it relies on the free Open-Meteo API service.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## IRC Server Details

Join us on MansionNET IRC to chat with us, test the bot, and play some trivia! 

🌐 **Server:** irc.inthemansion.com  
🔒 **Port:** 6697 (SSL)  
📝 **Channel:** #opers, #general, #welcome, #devs (and many others)

## Features

- Real-time weather information for any city worldwide
- Temperature, humidity, wind speed, and weather condition reporting
- SSL/TLS support for secure IRC connections
- Easy to configure and customize
- No API key required
- Rate limiting to prevent abuse

## Requirements

- Python 3.8 or higher
- `requests` library
- SSL-enabled IRC server

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MansionNET/weatherbot.git
cd weatherbot
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start the bot:
```bash
python weatherbot.py
```

### Available Commands

In any channel where the bot is present:

- `!weather <city>` - Get current weather for the specified city
  - Example: `!weather London`
  - Example: `!weather "New York"`
- `!help` - Display available commands


## API Information

WeatherBot uses two free APIs from Open-Meteo:
- [Geocoding API](https://open-meteo.com/en/docs/geocoding-api) for city lookup
- [Weather API](https://open-meteo.com/en/docs) for weather data

No API key is required, but please review their [terms of service](https://open-meteo.com/en/terms) before deployment.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Open-Meteo for providing free weather data
- The IRC community for continued support of the protocol

## Project Status

This project is actively maintained. If you encounter any issues or have suggestions, please open an issue on GitHub.
