import os
import threading
import socket
import random
import requests
import json
from mcstatus import MinecraftServer


filter_webhook = "" # discord webhook for servers with version filter
all_webhook = "" # discord webhook for all servers



# clear screen because why not
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

debug = True

# collored inputs
def inputl(text):
    value = input('\033[95m' + text + '\033[0m')
    return value

# collored prints
def printl(text):
    print('\033[95m' + text + '\033[0m')

# version filter
versionn = inputl("Version filter if dont want to filter leave empty :   ")

clear_screen()

# function name says it xd
def send_discord_webhook(embed, url):
    data = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    requests.post(url, json=data, headers=headers)



# function name says it xd
def check_minecraft_server(ip, port=25565, timeout=2):
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            sock.send(b'\xfe')
            data = sock.recv(1024)
            if len(data) > 0 and data[0] == 0xff:
                server_info = data[3:].decode('utf-16be')
                return True, server_info
            else:
                return False, "Not a Minecraft server"
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        return False, f"Connection failed: {e}"

# function name says it xd
def get_server_info(server_ip):
    try:
        server = MinecraftServer.lookup(server_ip)
        status = server.status()
        version = status.version.name
        online_players = status.players.online
        max_players = status.players.max
        player_names = [player.name for player in status.players.sample] if status.players.sample else []
        return version, online_players, max_players, player_names
    except Exception as e:
        if debug:
            printl(f"{server_ip} :cant get server infos because of :", e)
        return None, None, None, None

# function name says it xd
def check_and_get_server_info(ip):
    if debug:
        printl(f"checking ip:  {ip}")

    try:
        is_minecraft, server_info = check_minecraft_server(ip)
        if is_minecraft:
            version, online_players, max_players, player_names = get_server_info(ip)
            message = f"{ip} Name: {server_info}, Version: {version}, Spieler: {online_players}/{max_players}"
            printl(message)
            data = {
                "ip": ip,
                "server_info": server_info,
                "version": version,
                "online_players": online_players,
                "max_players": max_players,
                "player_names": player_names
            }
            with open('minecraft_servers.json', 'a') as json_file:
                json.dump(data, json_file, indent=4)
                json_file.write('\n')

                
            embed = {
                "title": 'Minecraft server',
                "description": f'Name: {server_info}\n\nPlayer: {online_players}/{max_players}\n\nIp: ```{"Hidden"}```\nVersion: {version}\nPlayer: {player_names}\nㅤ\n',
                "color": 0x15ff00,
                "thumbnail": {
                    "url": 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c7/Grass_Block.png',
                    "height": 0,
                    "width": 0
                },
                "footer": {
                    "text": 'Server Scanner',
                    "icon_url": 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c7/Grass_Block.png'
                }
            }
            if version == versionn or versionn in version:
                send_discord_webhook(embed, filter_webhook)
            else:
                send_discord_webhook(embed, all_webhook)
    except Exception as e:
        if debug:
            printl(f"erro in ip {ip}: {e}")

# function name says it xd
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# loop to search / check server while programm open
while True:
    ips = [generate_random_ip() for _ in range(50000)]
    threads = []
    for ip in ips:
        thread = threading.Thread(target=check_and_get_server_info, args=(ip,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
