# Minecraft-Server-Scanner

This Python script is designed to scan and check Minecraft servers, retrieve information about them, and send that information to a Discord webhook. It utilizes threading to perform the checks concurrently, enhancing the scanning speed.

## Features

- Generates random IP addresses to scan for Minecraft servers.
- Checks if an IP address is a Minecraft server.
- Retrieves server information such as version, online players, max players, and player names.
- Sends the server information to a Discord webhook.
- Supports filtering by Minecraft version.

## Requirements

- Python 3.x
- `requests` library
- `mcstatus` library

You can install the required libraries using pip:

```bash
pip install -r requirements.txt

