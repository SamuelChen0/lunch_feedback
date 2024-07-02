from flask import Flask, render_template
import subprocess
import threading
import time
import os

app = Flask(__name__)

game_process = None

def run_game():
    global game_process
    
    # Get the directory path of your JAR file
    jar_file_path = os.path.join(os.path.dirname(__file__), 'PlatformGameProject8.jar')
    print(f"JAR file path: {jar_file_path}")
    
    # Construct the Java command
    java_command = ['java', '-jar', jar_file_path]
    print(f"Java command: {' '.join(java_command)}")

    try:
        game_process = subprocess.Popen(java_command)
        print("Game process started successfully.")
    except Exception as e:
        print(f"Error starting game process: {e}")

def close_game_after_timeout():
    time.sleep(60)  # Change this to 60 seconds later
    if game_process and game_process.poll() is None:  # If the game process is still running
        game_process.terminate()  # Terminate the game process
        print("Game process terminated after timeout.")

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

@app.route('/stopgame')
def stop_game_route():
    global game_process
    
    if game_process and game_process.poll() is None:  # If the game process is still running
        game_process.terminate()  # Terminate the game process
        print("Game process stopped successfully.")
        return 'Java game stopped successfully!'
    else:
        return 'Game is not running!', 400

if __name__ == '__main__':
    app.run(debug=True)
