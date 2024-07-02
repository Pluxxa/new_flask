from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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
