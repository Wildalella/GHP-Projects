from flask import Flask, render_template # type: ignore

app = Flask(__name__)

img_link = "blank.jpg"
slide = 1
def move():
    global slide
    if slide == 5:
        slide = 4
    if slide == 1:
        img_link = "blank.jpg"
    if slide == 2:
        img_link = "blank.jpg"
    if slide == 3:
        img_link = "blank.jpg"
    if slide == 4:
        img_link = "blank.jpg"
move()

@app.route("/")
def home():
    return render_template('home.html', image= img_link)

@app.route("/team")
def team():
    return render_template('Team.html')

@app.route("/game")
def game():
    return render_template('Team.html')


if __name__ == '__main__':
    app.run(debug=True)