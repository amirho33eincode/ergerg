import os
from pyrogram import Client
from http.server import BaseHTTPRequestHandler

# Fetching environment variables
api_id = os.getenv('API_ID')  # Make sure to set this in your Vercel environment variables
api_hash = os.getenv('API_HASH')  # Make sure to set this in your Vercel environment variables
bot_token = os.getenv('BOT_TOKEN')  # Make sure to set this in your Vercel environment variables

# Initialize Pyrogram Client with environment variables
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Your logic to handle requests and interact with Telegram goes here
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Pyrogram bot is running!')

# Run your bot (Note: Vercel functions are stateless and should handle requests)
