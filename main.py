import discord
from discord.ext import commands
from mcstatus import JavaServer
import requests
from requests_html import HTMLSession
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
ip = os.environ.get("IP_ADDRESS")
TOKEN = os.environ.get("DC_BOT_TOKEN")
AUTH = os.environ.get("API_AUTHORIZATION")
server = JavaServer.lookup(ip)
url = f'https://api.freemcserver.net/v4/server/{ip[2:9]}/start'
headers = {
    'Authorization': f"{AUTH}"
}

bot = commands.Bot(command_prefix='mist', intents=discord.Intents.all())


def check_renew():
    session = HTMLSession()
    state_url = f'https://freemcserver.net/server/{ip[2:9]}'
    state_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    page = session.get(state_url, headers=state_headers)
    selector = 'p:contains("Server Expires on:") b'
    state = page.html.find(selector=selector, first=True)
    if state.text != 'Initializing countdown...':
        given_time_str = state.text
        given_time = datetime.strptime(given_time_str, "%Y-%m-%d %H:%M:%S %Z")
        current_time = datetime.utcnow()
        time_difference = given_time - current_time
        print(f"Time difference: {time_difference}")
        threshold = timedelta(minutes=30)
        if time_difference < threshold:
            return time_difference, False
        else:
            return time_difference, True
    else:
        return '0', False


@bot.event
async def on_ready():
    print('Logged in.'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)


@bot.tree.command(name='start', description='Starts the server.')
async def chat(interaction: discord.Interaction):
    x = requests.post(url, headers=headers, timeout=10)
    started = x.json()['success']
    if started is True:
        await interaction.response.send_message("Server is starting...")
    else:
        error = x.json()['error']
        await interaction.response.send_message(f"You got an error nigga. {error}.")


@bot.tree.command(name='status', description='Tells the status of the server.')
async def chat(interaction: discord.Interaction):
    try:
        status = server.status()
        await interaction.response.send_message(
            f"Server is online with `{status.players.online} of {status.players.max}` players. IP Address is `{ip}`!")
    except:
        time_d, renew_state = check_renew()
        time_delta = datetime.strptime(str(time_d), "%H:%M:%S.%f")
        stylized_time = f'{time_delta.hour} hours, {time_delta.minute} minutes and {time_delta.second} seconds'
        if renew_state:
            await interaction.response.send_message(f"Server is either offline or turning on. Time left to renew is `{stylized_time}`.")
        else:
            await interaction.response.send_message("Server expiring or expired. Please renew it at https://freemcserver.net/server/1131697/renew")

bot.run(TOKEN)
