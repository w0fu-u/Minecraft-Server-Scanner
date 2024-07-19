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
```
## Configuration
Discord Webhooks
You need to configure two Discord webhooks in the script:

- `filter_webhook`: Webhook URL for servers that match the specified version filter.
- `all_webhook`: Webhook URL for all servers regardless of the version.


![Alt-Text](https://cdn.discordapp.com/attachments/1257786688688754800/1263887556236414996/image.png?ex=669bde83&is=669a8d03&hm=dbf0da545ea49930652d256087ee825c5b111a8a78b042d5c9747046e469afa4&)

## Version Filter
You can specify a version filter to only send information about servers running a specific Minecraft version. If you don't want to filter by version, leave this field empty.

## Example Output
The script will print server information to the console and send it to the configured Discord webhooks. It will also save the information to a JSON file named `minecraft_servers.json`.

```json
{
    "ip": "192.168.1.1",
    "server_info": "Minecraft Server",
    "version": "1.16.5",
    "online_players": 5,
    "max_players": 20,
    "player_names": ["Player1", "Player2"]
}
```

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## Contact
For any inquiries or feedback, please contact on Discord `@wofu_u`.
