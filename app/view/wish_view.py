from flask import Blueprint, request, jsonify
from app.controller.wish_controller import (add_wish_logic, remove_wish_logic, get_wish_logic, get_all_wishes_logic, like_wish_logic, remove_all_wishes_logic)

views = Blueprint('views', __name__)

@views.route('/add_wish', methods=['POST'])
def add_wish():
    """
    Adds a new wish
    ---
    tags:
      - Wishes
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - content
          properties:
            content:
              type: string
    responses:
      201:
        description: Wish added successfully
      400:
        description: Invalid input
    """

    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'message': 'Content is required'}), 400
    new_wish = add_wish_logic(content)
    return jsonify({'message': 'Wish added successfully', 'id': new_wish.id}), 201

@views.route('/wishes/<int:wish_id>', methods=['DELETE'])
def remove_wish(wish_id):
    """
    Removes a specific wish
    ---
    tags:
      - Wishes
    parameters:
      - name: wish_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Wish removed successfully
      404:
        description: Wish not found
    """

    wish = remove_wish_logic(wish_id)
    if wish:
        return jsonify({'message': 'Wish removed successfully'}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

@views.route('/wishes/<int:wish_id>', methods=['GET'])
def get_wish(wish_id):
    """
    Retrieves a specific wish by its ID
    ---
    tags:
      - Wishes
    parameters:
      - name: wish_id
        in: path
        type: integer
        required: true
        description: Unique ID of the wish
    responses:
      200:
        description: Wish found and returned
      404:
        description: Wish not found
    """

    wish = get_wish_logic(wish_id)
    if wish:
        return jsonify({'id': wish.id, 'content': wish.content, 
                        'timestamp': wish.timestamp, 'likes': wish.likes}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

@views.route('/wishes', methods=['GET'])
def get_all_wishes():
    """
    Retrieves all wishes
    ---
    tags:
      - Wishes
    responses:
      200:
        description: List of all wishes
    """

    wishes = get_all_wishes_logic()
    return jsonify([{'id': wish.id, 'content': wish.content, 'timestamp': wish.timestamp, 'likes': wish.likes} for wish in wishes]), 200

@views.route('/wishes/<int:wish_id>/like', methods=['POST'])
def like_wish(wish_id):
    """
    Likes a specific wish
    ---
    tags:
      - Wishes
    parameters:
      - name: wish_id
        in: path
        type: integer
        required: true
        description: Unique ID of the wish to be liked
    responses:
      200:
        description: Wish liked successfully
      404:
        description: Wish not found
    """

    wish = like_wish_logic(wish_id)
    if wish:
        return jsonify({'message': 'Wish liked successfully', 'likes': wish.likes}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

@views.route('/wishes', methods=['DELETE'])
def remove_all_wishes():
    """
    Removes all wishes
    ---
    tags:
      - Wishes
    responses:
      200:
        description: All wishes removed successfully
      500:
        description: Internal server error
    """
    
    result = remove_all_wishes_logic()
    if isinstance(result, int):
        return jsonify({'message': f'{result} wishes removed successfully'}), 200
    else:
        return jsonify({'error': result}), 500