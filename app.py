from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_survey', methods=['GET', 'POST'])
def create_survey():
    if request.method == 'POST':
        # Handle survey submission here
        pass
    return render_template('create_survey.html')

@app.route('/access_survey', methods=['GET', 'POST'])
def access_survey():
    if request.method == 'POST':
        # Handle survey access here
        pass
    return render_template('access_survey.html')

if __name__ == '__main__':
    app.run(debug=True)