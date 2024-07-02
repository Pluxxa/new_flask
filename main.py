from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(current_time=current_time)

@app.route("/tom_cruze/")
def index_1():
    return render_template("index_2.html")

@app.route("/kianu/")
def index_2():
    return render_template("index_3.html")

@app.route("/ddepp/")
def index_3():
    return render_template("index_4.html")

if __name__ == "__main__":
    app.run()
