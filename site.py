from flask import Flask, render_template, flash, redirect, url_for, session, request


app = Flask(__name__)
app.secret_key = "blogum"



@app.route("/")
def index():
    return render_template("index.html",articles=articles,)

@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/articles")
def articles():
   return render_template("articles.html")



if __name__ == "__main__":
    app.run(debug=True)
