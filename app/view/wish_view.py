from flask import Blueprint, request, jsonify
from app.controller.wish_controller import (add_wish_logic, remove_wish_logic, get_wish_logic, get_all_wishes_logic, like_wish_logic)

views = Blueprint('views', __name__)

@views.route('/add_wish', methods=['POST'])
def add_wish():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'message': 'Content is required'}), 400
    new_wish = add_wish_logic(content)
    return jsonify({'message': 'Wish added successfully', 'id': new_wish.id}), 201

@views.route('/wishes/<int:wish_id>', methods=['DELETE'])
def remove_wish(wish_id):
    wish = remove_wish_logic(wish_id)
    if wish:
        return jsonify({'message': 'Wish removed successfully'}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

@views.route('/wishes/<int:wish_id>', methods=['GET'])
def get_wish(wish_id):
    wish = get_wish_logic(wish_id)
    if wish:
        return jsonify({'id': wish.id, 'content': wish.content, 
                        'timestamp': wish.timestamp, 'likes': wish.likes}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

@views.route('/wishes', methods=['GET'])
def get_all_wishes():
    wishes = get_all_wishes_logic()
    return jsonify([{'id': wish.id, 'content': wish.content, 'timestamp': wish.timestamp, 'likes': wish.likes} for wish in wishes]), 200

@views.route('/wishes/<int:wish_id>/like', methods=['POST'])
def like_wish(wish_id):
    wish = like_wish_logic(wish_id)
    if wish:
        return jsonify({'message': 'Wish liked successfully', 'likes': wish.likes}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404
