from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from routes import weather_bp

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["20 per minute"]
)

app.register_blueprint(weather_bp)


@app.route("/")
def home():
    return {
        "message": "Weather API Running"
    }


if __name__ == "__main__":
    app.run(debug=True)