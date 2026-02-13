import os
import subprocess
import threading
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return "iSponsorBlockTV is running 24/7!", 200

def run_main_script():
    while True:
        print("Starting iSponsorBlockTV (src/main.py)...")
        try:
            # This starts the script and waits for it to finish/crash
            subprocess.run(["python", "src/main.py"], check=True)
        except Exception as e:
            print(f"Script crashed with error: {e}")
        
        print("Restarting script in 60 seconds...")
        time.sleep(60) # Wait 60 seconds before restarting if it crashes

if __name__ == "__main__":
    # Start the background loop in a separate thread
    threading.Thread(target=run_main_script, daemon=True).start()
    
    # Start the Flask server so Render/Cron-job can ping it
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
