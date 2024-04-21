from flask import Flask, render_template, request
import subprocess
import threading
import time

app = Flask(__name__)

game_process = None
last_interaction_time = None

import subprocess

def run_game():
    global game_process
    # This java command needs to be changed since it is different for every single device
    java_command = [
    # Java Executable Path
    r'C:\Program Files\Eclipse Adoptium\jdk-21.0.2.13-hotspot\bin\java.exe',
    # Java VM Option
    '-XX:+ShowCodeDetailsInExceptionMessages',
    # Classpath Option
    '-cp',
    # Classpath Value
    r'C:\Users\admin\PlatformGameProject\bin',
    # Main Class to Run
    'main.java.com.example.Main'
]

    game_process = subprocess.Popen(java_command)

def close_game_after_timeout():
    global game_process, last_interaction_time
    while True:
        if last_interaction_time is not None:
            time_diff = time.time() - last_interaction_time
            if time_diff >= 10:  # If there's no interaction for 10 seconds
                if game_process and game_process.poll() is None:  # If the game process is still running
                    game_process.terminate()  # Terminate the game process
                last_interaction_time = None  # Reset last_interaction_time
        time.sleep(1)

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

@app.route('/interaction', methods=['POST'])
def record_interaction():
    global last_interaction_time
    last_interaction_time = time.time()
    return 'Interaction recorded!'

if __name__ == '__main__':
    app.run(debug=True)
