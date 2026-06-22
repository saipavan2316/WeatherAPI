from flask import Blueprint, jsonify

from services.weather_service import fetch_weather

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather/<city>", methods=["GET"])
def get_weather(city):

    result = fetch_weather(city)

    if "error" in result:
        return jsonify(result), 404

    return jsonify(result)