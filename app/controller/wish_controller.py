from app.model.wish import Wish
from flask import request, jsonify
from app.extensions import db

def add_wish():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'message': 'Content is required'}), 400

    new_wish = Wish(content=content)
    db.session.add(new_wish)
    db.session.commit()
    return jsonify({'message': 'Wish added successfully', 'id': new_wish.id}), 201

def remove_wish(wish_id):
    wish = Wish.query.get(wish_id)
    if wish:
        db.session.delete(wish)
        db.session.commit()
        return jsonify({'message': 'Wish removed successfully'}), 200
    else:
        return jsonify({'message': 'Wish not found'}), 404

