from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)












if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True