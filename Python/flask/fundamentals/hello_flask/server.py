from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", phrase="smooch", times=100000)


@app.route('/success')
def success():
    return "success"


@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name


@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
