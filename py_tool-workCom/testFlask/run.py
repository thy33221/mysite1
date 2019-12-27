
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template('base.html', words="1Tester ,Hello World! ")



if __name__ == "__main__":
    app.run(port=1991,debug=True)