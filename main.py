from flask import Flask, render_template as rt

app = Flask("Website")


@app.route("/")
def home():
    return rt("home.html")
@app.route("/about/")
def about():
    return rt("about.html")


app.run(debug=True)
