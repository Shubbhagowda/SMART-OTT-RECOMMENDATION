# routes.py

from flask import Blueprint, request, jsonify

from recommendation.recommendation_engine import (
    get_recommendations
)

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)


@recommendation_bp.route(
    "/api/recommendations",
    methods=["POST"]
)
def recommend():

    try:

        user_data = request.get_json(silent=True)

        if not isinstance(user_data, dict):
            return jsonify({
                "success": False,
                "message": "Please send valid JSON data."
            }), 400

        results = get_recommendations(user_data)

        return jsonify({
            "success": True,
            "count": len(results),
            "recommendations": results
        }), 200

    except ValueError as error:

        return jsonify({
            "success": False,
            "message": str(error)
        }), 400

    except Exception as error:

        return jsonify({
            "success": False,
            "message": "Could not generate recommendations."
        }), 500