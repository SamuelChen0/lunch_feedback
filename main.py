from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the click count to zero
click_count = 0

@app.route('/')
def home():
    return render_template('index.html', click_count=click_count)

@app.route('/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
