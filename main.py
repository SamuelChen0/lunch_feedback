from flask import Flask, render_template
import os
import subprocess
import threading
import time

app = Flask(__name__)

game_process = None

import subprocess

def run_game():
    global game_process

    # Retrieve the Java command from the environment variable
    java_command = os.getenv('JAVA_COMMAND')

    # Check if the environment variable is set
    if java_command is None:
        print("Error: JAVA_COMMAND environment variable is not set.")
        return

    # Run the Java command
    try:
        game_process = subprocess.Popen(java_command, shell=True)
        game_process.wait()  # Wait for the process to finish
    except Exception as e:
        print("Error running the game:", e)

    game_process = subprocess.Popen(java_command)

def close_game_after_timeout():
    time.sleep(60)  # Change this to 60 seconds later
    if game_process and game_process.poll() is None:  # If the game process is still running
        game_process.terminate()  # Terminate the game process

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rungame')
def run_game_route():
    global game_process

    if game_process and game_process.poll() is None:  # If the game process is already running
        return 'Game is already running!'

    run_game()  # Run the game

    timeout_thread = threading.Thread(target=close_game_after_timeout)
    timeout_thread.start()
    print("Game is running")

    return 'Java game started!'

if __name__ == '__main__':
    app.run(debug=True)