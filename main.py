from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def run_game():
    java_command = [
        'C:\\Program Files\\Eclipse Adoptium\\jdk-21.0.2.13-hotspot\\bin\\java.exe',
        '-XX:+ShowCodeDetailsInExceptionMessages',
        '-cp',
        'C:\\Users\\admin\\PlatformGameProject\\bin',
        'main.java.com.example.Main'
    ]

    subprocess.run(java_command, shell=True)

    return 'Java game started!'
# def index():
#     return render_template('index.html')

#@app.route('/rungame')

if __name__ == '__main__':
    app.run(debug=True)
