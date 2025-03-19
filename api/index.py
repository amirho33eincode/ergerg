import os
from pyrogram import Client, filters
from flask import Flask

# Fetching environment variables
api_id = os.getenv('API_ID')  # Set this in your environment variables
api_hash = os.getenv('API_HASH')  # Set this in your environment variables
bot_token = os.getenv('BOT_TOKEN')  # Set this in your environment variables

# Initialize Pyrogram Client with environment variables
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Initialize Flask app
flask_app = Flask(__name__)

@app.on_message(filters.command("start"))  # Listen for /start command
def start_command(client, message):
    # Use client.send_message to send a message to the chat
    return "FUCKING"

@flask_app.route("/")
def home():
    return "Pyrogram bot is running!"

# Start the bot and Flask app
if __name__ == "__main__":
    # Run the bot in a separate thread
    app.start()
    flask_app.run(port=5000)  # Default port for Vercel apps
