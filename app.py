from flask import Flask  # Import the Flask web framework

app = Flask(__name__)    # Initialize the web application


@app.route("/")          # Map the main website URL (/) to the home function
def home():
    return "Hello for DevOps CI Project! Running from the AWS Instance"  # Text shown on the website screen


if __name__ == "__main__":
    # Run server on port 5000 and allow external connections (needed for Docker)
    app.run(host="0.0.0.0", port=5000)
