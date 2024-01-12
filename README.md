
# fms Discord Bot

This is a Discord bot which can interact with the members in your server to start, and get the details of your minecraft server hosted on freemcserver.net. It also provides a link to renew the server if the countdown is too low or expired. **Keep in mind that this is an unofficial bot and has no relation with the website or its owner(s), using this code WILL GET YOU BANNED. Use it at your own risk.**




## Prerequisites

* Python 3.x
* requirements.txt
* A server on freemcserver.net
## Installation

1. Clone the repository:

```bash
git clone https://github.com/FoxGoesBrrr/fmsDiscordBot.git
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
3. Set up your bot by filling in the `.env` file with the IP Address of the server, your discord bot token and your fms authorization token (this can be found by scanning the login QR code in mobile section of the website).

4. Run the bot.
```bash
python main.py 
```
## Usage

#### Starting  a server ####
```bash
/start
```

This command will start the server if its not started. In case the server is already running, it will suggest the user to join the server providing the IP Address of the server.

#### Getting status of a server ####
````bash
/status
````

This command will give the status of the server, and tell the times remaining for the next renewal. This command might break if the server is offline for too long.
## Acknowledgements

 - [discord.py](https://discordpy.readthedocs.io/)
 - [freemcserver.net](https://freemcserver.net/)
 - [requests](https://requests.readthedocs.io/en/latest/)
 - [requests-html](https://requests.readthedocs.io/projects/requests-html/en/latest/)

## Contributing

Feel free to contribute to the development of this bot by forking the repository and creating pull requests. If you encounter any issues or have suggestions, please open an issue in the GitHub repository.
