from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, GitHub Actions!"

if __name__ == "__main__":
    app.run()


message (e.g., "Add app.py")
