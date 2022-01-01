from flask import Flask, render_template, request, redirect, session
from flask.templating import render_template_string

app = Flask(__name__)
app.secret_key = "0Wy*p*0YrR{7N.2v#a0Aw$0qJ"



@app.route("/")
def home():
    if session["session_number"] >= 0:
        session["session_number"] += 1
    else:
        session["session_number"] = 0
        
    return render_template("index.html")

@app.route("/count", methods = ["POST"])
def count_session():
    return redirect("/")


@app.route("/destroy_session", methods = ["POST"])
def reset_session():
    session.clear()
    session["session_number"] = -1
    
    return redirect('/')











if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True