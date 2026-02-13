from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def health_check():
    return "I am alive!", 200

def your_original_script():
    while True:
        print("Your background task is running...")
        time.sleep(60)

if __name__ == "__main__":
    # Run your background task in a separate thread
    threading.Thread(target=your_original_script, daemon=True).start()
    # Start the Flask server
    app.run(host='0.0.0.0', port=10000)
