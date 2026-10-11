import time
from javascript import require

mineflayer = require('mineflayer')

def start_bot():
    while True:
        try:
            print("Connecting to Aternos server...")
            bot = mineflayer.createBot({
                'host': 'anAs11ha-GiMI.aternos.me',
                'port': 24414,
                'username': 'AFK_Guard_247'
            })

            @bot.on('spawn')
            def handle_spawn(this):
                print("Bot joined successfully!")

            @bot.on('end')
            def handle_end(this, reason):
                print(f"Disconnected: {reason}. Reconnecting...")

            @bot.on('error')
            def handle_error(this, err):
                print(f"Error: {err}")

            time.sleep(86400)

        except Exception as e:
            print(f"Connection failed: {e}. Retrying...")
            time.sleep(10)

if __name__ == "__main__":
    start_bot()
