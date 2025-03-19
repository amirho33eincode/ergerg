import os
from pyrogram import Client, filters

# Fetching environment variables
api_id = os.getenv('API_ID')  # Set this in your environment variables
api_hash = os.getenv('API_HASH')  # Set this in your environment variables
bot_token = os.getenv('BOT_TOKEN')  # Set this in your environment variables

# Initialize Pyrogram Client with environment variables
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))  # Listen for /start command
def start_command(client, message):
    # Use client.send_message to send a message to the chat
    chat_id = message.chat.id  # Get the chat ID
    client.send_message(chat_id, "Hello! Your bot has started! 😊")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Your logic to handle requests and interact with Telegram goes here
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Pyrogram bot is running!')



# Start the bot
if __name__ == "__main__":
    app.run()  # Start the bot

