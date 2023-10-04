from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the click count to zero
click_count1STAR = 0
click_count2STAR = 0
click_count3STAR = 0
click_count4STAR = 0
click_count5STAR = 0

@app.route('/')
def home():
    return render_template('index.html', click_count1STAR=click_count1STAR, click_count2STAR=click_count2STAR, click_count3STAR=click_count3STAR, click_count4STAR=click_count4STAR, click_count5STAR=click_count5STAR)

@app.route('/click1star', methods=['POST'])
def click1():
    global click_count1STAR
    click_count1STAR += 1
    return 'success'
@app.route('/click2star', methods=['POST'])
def click2():
    global click_count2STAR
    click_count2STAR += 1
    return 'success'
@app.route('/click3star', methods=['POST'])
def click3():
    global click_count3STAR
    click_count3STAR += 1
    return 'success'
@app.route('/click4star', methods=['POST'])
def click4():
    global click_count4STAR
    click_count4STAR += 1
    return 'success'
@app.route('/click5star', methods=['POST'])
def click5():
    global click_count5STAR
    click_count5STAR += 1
    return 'success'
if __name__ == '__main__':
    app.run(debug=True)
