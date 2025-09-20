from flask import Flask, request, render_template

app = Flask(__name__)

VALID_NAME = "devops"
VALID_PASSWORD = "password123"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form.get("username","")
    password = request.form.get("password","")

    if username == VALID_NAME and password == VALID_PASSWORD:
        return "Login success",200
    else:
        return "Login failed",401

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

