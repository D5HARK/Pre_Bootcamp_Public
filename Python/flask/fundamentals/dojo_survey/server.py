from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "0Wy*p*0YrR{7N.2v#a0Aw$0J"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods=["POST"])
def handle_data():
    session.clear()
    session["user_name"] = request.form["name"]
    session["user_location"] = request.form["location"]
    session["user_language"] = request.form["language"]
    session["user_about"] = request.form["about"]
    return redirect("/show")

@app.route("/show")
def show_page(): 
    return render_template("show.html")



if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True