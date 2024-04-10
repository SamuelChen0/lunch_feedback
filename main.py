from flask import Flask, render_template
import subprocess
import threading
import time

app = Flask(__name__)

game_process = None

import subprocess

def run_game():
    global game_process
    # This java command needs to be changed since it is different for every single device
    java_command = [
        r'C:\Program Files\Java\jdk-21\bin\java.exe',  # Path to java executable
        '-XX:+ShowCodeDetailsInExceptionMessages',     # Java VM option
        '-cp',                                          # Classpath option
        r'C:\Users\alfee\PlatformGameProject\bin',     # Classpath value
        'main.java.com.example.Main'                   # Main class to run
    ]

    game_process = subprocess.Popen(java_command)

def close_game_after_timeout():
    time.sleep(20)  # Wait for twenty seconds
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

    return 'Java game started!'

if __name__ == '__main__':
    app.run(debug=True)
