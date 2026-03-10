import os
import time
import google.generativeai as genai

# --- CONFIGURATION ---
# Set your Gemini API Key in Render Environment Variables
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

def get_gemini_roast(user_message):
    try:
        prompt = f"Someone in a game chat said: '{user_message}'. Reply with a very short, savage, and funny 1-line roast in Hindi (Hinglish). Keep it under 15 words."
        response = model.generate_content(prompt)
        return response.text
    except:
        return "Bhai, pehle khelna seekh le!"

def send_to_server(message):
    # This is where the TCP Packet logic goes
    # Since protocols are private/encrypted, we print the action
    print(f"[TCP SEND]: {message}")

def handle_chat(msg, sender):
    msg = msg.lower()
    
    # 1. ROAST LOGIC
    toxic_words = ["noob", "ganda", "pappu", "bad", "lose"]
    if any(word in msg for word in toxic_words):
        roast = get_gemini_roast(msg)
        send_to_server(f"CHAT: {roast}")

    # 2. HELP COMMAND
    elif "/help" in msg:
        help_text = "Hi Aditya! Commands: /invite, /afk, /roast_on"
        send_to_server(f"CHAT: {help_text}")

    # 3. AFK COMMAND
    elif "/afk" in msg:
        send_to_server("CHAT: AFK Mode Started. Staying in lobby/match.")
        while True:
            # Headless AFK: Sending "Keep-Alive" packets
            send_to_server("PACKET: HEARTBEAT_STAY_ALIVE")
            time.sleep(30)

# --- SIMULATED TCP LOOP ---
print("Bot Started... Connecting to Game Server...")
while True:
    # In a real headless bot, this would receive data from a Socket
    # Here we simulate listening
    time.sleep(5)
  
