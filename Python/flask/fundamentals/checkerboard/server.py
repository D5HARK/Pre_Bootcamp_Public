from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def eight_by():
    return render_template("index.html", x_size = 8, y_size = 8, color_1 = "red", color_2 = "blue")

@app.route('/<y_input>')
def y_by(y_input):
    return render_template("index.html", x_size = 8, y_size = int(y_input), color_1 = "red", color_2 = "blue")

@app.route('/<x_input>/<y_input>')
def x_y_by(x_input, y_input):
    return render_template("index.html", x_size = int(x_input), y_size = int(y_input), color_1 = "red", color_2 = "blue")

@app.route("/<x_input>/<y_input>/<color_one_input>/<color_two_input>")
def custom_site(x_input, y_input, color_one_input, color_two_input):
    return render_template("index.html", x_size = int(x_input), y_size = int(y_input), color_1 = color_one_input, color_2 = color_two_input)


if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True


