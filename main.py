from flask import Flask, render_template
import subprocess
import threading
import time
import os

app = Flask(__name__)

game_process = None
cleanup_done = False

def run_game():
    global game_process
    
    # Get the directory path of your JAR file
    jar_file_path = os.path.join(os.path.dirname(__file__), 'PlatformGameProject.jar')
    print(f"JAR file path: {jar_file_path}")
    
    # Construct the Java command
    java_command = ['java', '-jar', jar_file_path]
    print(f"Java command: {' '.join(java_command)}")

    try:
        game_process = subprocess.Popen(java_command)
        print("Game process started successfully.")
    except Exception as e:
        print(f"Error starting game process: {e}")

def close_game():
    global game_process
    if game_process and game_process.poll() is None:  # If the game process is still running
        game_process.terminate()  # Terminate the game process
        print("Game process terminated.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rungame')
def run_game_route():
    global game_process

    if game_process and game_process.poll() is None:  # If the game process is already running
        print("Game is already running!")
        return 'Game is already running!'

    run_game()  # Run the game
    
    # Start the cleanup timer if it hasn't been started yet!
    global cleanup_done
    if not cleanup_done:
        cleanup_thread = threading.Thread(target=close_game_after_timeout)
        cleanup_thread.start()
        cleanup_done = True

    return 'Java game started!'

@app.route('/stopgame')
def stop_game_route():
    global cleanup_done

    if not cleanup_done:
        print("No game is running!")
        return 'No game is running!'

    close_game()
    cleanup_done = False
    print("Java game stopped.")
    return 'Java game stopped!'

def close_game_after_timeout():
    global cleanup_done
    if not cleanup_done:
        time.sleep(60)  # Change this to 60 seconds later
        close_game()
        cleanup_done = True

if __name__ == '__main__':
    app.run(debug=True)
