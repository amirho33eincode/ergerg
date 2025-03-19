import os
from pyrogram import Client
from http.server import BaseHTTPRequestHandler

# Fetching environment variables
api_id = os.getenv('API_ID')  # Make sure to set this in your Vercel environment variables
api_hash = os.getenv('API_HASH')  # Make sure to set this in your Vercel environment variables
bot_token = os.getenv('BOT_TOKEN')  # Make sure to set this in your Vercel environment variables

# Initialize Pyrogram Client with environment variables
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a hello message
def send_hello_message():
    # Replace 'YOUR_CHAT_ID' with your actual chat ID or username
    app.send_message("YOUR_CHAT_ID", "Hello! Your bot has started!")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Your logic to handle requests and interact with Telegram goes here
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Pyrogram bot is running!')

# On starting the bot, send a hello message
with app:
    send_hello_message()
    app.run()  # Start the bot

# Note: Make sure 'YOUR_CHAT_ID' is replaced with your actual chat ID (you can get your chat ID by sending a message to the bot and then using `app.get_updates()` or any other method to retrieve it).
