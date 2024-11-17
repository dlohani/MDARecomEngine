from flask import Blueprint, request, jsonify
from app.services.recommendation import get_recommendations
from app import redis

bp = Blueprint('recommendations', __name__, url_prefix='/recommendations')

@bp.route('/<int:user_id>', methods=['GET'])
def recommend(user_id):
    recommendations = get_recommendations(user_id, redis)
    return jsonify({
        'user_id': user_id,
        'recommendations': recommendations
    })
