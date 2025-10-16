from flask import Flask, render_template, url_for
from regression.regression_model import run_regression

app = Flask(__name__)

@app.route('/')
def index():
    results = run_regression()
    image_url = url_for('static', filename='hasil_regresi.png')
    return render_template('index.html', results=results, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
