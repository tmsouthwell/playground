from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play_one():
    return render_template("index.html", num=3, color="lightskyblue")

@app.route('/play/<int:num>')
def play_two(num):
    return render_template("index.html", num = num, color="lightskyblue")

@app.route('/play/<int:num>/<string:color>')
def play_three(num, color):
    return render_template("index.html", num = num, color=color)


if __name__=="__main__":
    app.run(debug=True)

