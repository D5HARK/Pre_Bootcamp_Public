from flask import Flask, render_template
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)