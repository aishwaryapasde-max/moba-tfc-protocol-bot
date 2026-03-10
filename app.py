import os
from flask import Flask
import google.generativeai as genai
import threading
import time

app = Flask(__name__)

# --- GEMINI SETUP ---
# You will add your API Key in Render's Dashboard (Environment Variables)
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- BOT LOGIC ---
def get_roast(text):
    prompt = f"Someone said '{text}' in a game. Give a savage 1-line Hindi roast (Hinglish). Short and funny."
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "Beta, pehle khelna seekh lo!"

def bot_loop():
    """This function simulates the headless TCP connection"""
    print("Headless TCP Bot: Connecting to Server...")
    while True:
        # This is where your TCP 'Keep-Alive' packets go
        # For now, it keeps the process alive
        print("Bot Status: Online & Listening...")
        time.sleep(60)

# --- WEB ROUTES ---
@app.route('/')
def home():
    return "TFC Bot is Running 24/7"

if __name__ == "__main__":
    # Start the bot in a background thread
    threading.Thread(target=bot_loop, daemon=True).start()
    # Start the web server
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
