from flask import Flask, render_template

app = Flask(__name__)


class Sample:
    def __init__(self):
        pass

    def calcAdd(self, x, y):
        return x + y


@app.route("/", methods=["GET", "POST"])
def main_page():
    board = [1, 2, 3]
    return render_template("lifegame.html", board=board)
