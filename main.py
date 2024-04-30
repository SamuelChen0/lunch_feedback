from flask import Flask, render_template
import subprocess
import threading
import time
import os
import sys

app = Flask(__name__)

game_process = None
cleanup_done = False

def run_game():
    global game_process
    
    # Get the directory path of your compiled Java files on PythonAnywhere
    java_files_directory = os.path.join(sys.path[0], 'PlatformGameProject', 'bin')  # Assuming 'bin' is the directory containing compiled .class files
    
    # Construct the classpath dynamically
    classpath = java_files_directory
    
    # Construct the Java command
    java_command = [
        'java',  # Use 'java' command directly
        '-XX:+ShowCodeDetailsInExceptionMessages',
        '-cp',
        classpath,
        'main.java.com.example.Main'  # Update the package and main class name if needed
    ]

    game_process = subprocess.Popen(java_command)

def close_game():
    global game_process
    if game_process and game_process.poll() is None:  # If the game process is still running
        game_process.terminate()  # Terminate the game process

def close_game_after_timeout():
    global cleanup_done
    if not cleanup_done:
        time.sleep(60)  # Change this to 60 seconds later
        close_game()
        cleanup_done = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rungame')
def run_game_route():
    global game_process

    if game_process and game_process.poll() is None:  # If the game process is already running
        return 'Game is already running!'

    run_game()  # Run the game
    
    # Start the cleanup timer if it hasn't been started yet!
    global cleanup_done
    if not cleanup_done:
        cleanup_thread = threading.Thread(target=close_game_after_timeout)
        cleanup_thread.start()
        cleanup_done = True

    return 'Java game started!'

if __name__ == '__main__':
    app.run(debug=True)
