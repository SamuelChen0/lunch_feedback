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
    # Java Executable Path
       r'C:\Program Files\Java\jdk-21\bin\java.exe',
    # Java VM Option
    '-XX:+ShowCodeDetailsInExceptionMessages',
    # Classpath Option
    '-cp',
    # Classpath Value
    r'C:\Users\alfee\PlatformGameProject\bin',
    # Main Class to Run
    'main.java.com.example.Main'
]

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