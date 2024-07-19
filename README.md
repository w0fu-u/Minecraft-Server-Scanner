# Minecraft-Server-Scanner
This Python script is designed to scan and check Minecraft servers, retrieve information about them, and send that information to a Discord webhook. It utilizes threading to perform the checks concurrently, enhancing the scanning speed.

Features
Generates random IP addresses to scan for Minecraft servers.
Checks if an IP address is a Minecraft server.
Retrieves server information such as version, online players, max players, and player names.
Sends the server information to a Discord webhook.
Supports filtering by Minecraft version.
Requirements
Python 3.x
requests library
mcstatus library
You can install the required libraries using pip:

bash
Copy code
pip install requests mcstatus
Configuration
Discord Webhooks
You need to configure two Discord webhooks in the script:

filter_webhook: Webhook URL for servers that match the specified version filter.
all_webhook: Webhook URL for all servers regardless of the version.
Version Filter
You can specify a version filter to only send information about servers running a specific Minecraft version. If you don't want to filter by version, leave this field empty.

Usage
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/minecraft-server-scanner.git
Navigate to the project directory:
bash
Copy code
cd minecraft-server-scanner
Run the script:
bash
Copy code
python server_scanner.py
Example Output
The script will print server information to the console and send it to the configured Discord webhooks. It will also save the information to a JSON file named minecraft_servers.json.

json
Copy code
{
    "ip": "192.168.1.1",
    "server_info": "Minecraft Server",
    "version": "1.16.5",
    "online_players": 5,
    "max_players": 20,
    "player_names": ["Player1", "Player2"]
}
Script Details
Functions
clear_screen(): Clears the terminal screen.
inputl(text): Colored input prompt.
printl(text): Colored print statement.
send_discord_webhook(embed, url): Sends an embed to the specified Discord webhook.
check_minecraft_server(ip, port=25565, timeout=2): Checks if an IP address is a Minecraft server.
get_server_info(server_ip): Retrieves server information using mcstatus.
check_and_get_server_info(ip): Combines checking and retrieving server information, sends the data to Discord, and saves it to a JSON file.
generate_random_ip(): Generates a random IP address.
Main Loop
The script continuously generates random IP addresses, checks if they are Minecraft servers, retrieves their information, and sends the data to the Discord webhooks.


Contact
For any inquiries or feedback, contact on Discord [@wofu_u].
