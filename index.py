from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name="John Doe", description="I am a software engineer.")

if __name__ == "__main__":
    app.run()
