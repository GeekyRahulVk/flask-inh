from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/inh')
def home():
    return render_template("inh.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post')
def post():
    return render_template("post.html")




if __name__ == "__main__":
    app.run()
	  