from flask import Flask, render_template
import subprocess
import threading
import time

app = Flask(__name__)

game_process = None

def run_game():
    global game_process
    java_command = [
        'C:\\Program Files\\Eclipse Adoptium\\jdk-21.0.2.13-hotspot\\bin\\java.exe',
        '-XX:+ShowCodeDetailsInExceptionMessages',
        '-cp',
        'C:\\Users\\admin\\PlatformGameProject\\bin',
        'main.java.com.example.Main'
    ]

    game_process = subprocess.Popen(java_command)

def close_game_after_timeout():
    time.sleep(20)  # Wait for one minute
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

    game_thread = threading.Thread(target=run_game)
    game_thread.start()

    timeout_thread = threading.Thread(target=close_game_after_timeout)
    timeout_thread.start()

    return 'Java game started!'

if __name__ == '__main__':
    app.run(debug=True)
