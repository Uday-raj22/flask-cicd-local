from flask import Flask, render_template
from lorenz import generate_lorenz_plot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lorenz")
def lorenz():
    img_path = "static/img/lorenz.png"
    generate_lorenz_plot(img_path)
    return render_template("lorenz.html")

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

