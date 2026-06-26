from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static", "Flappy_Spikes.html")

@app.after_request
def add_headers(response):
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)




if __name__ == "__main__":
    app.run()
