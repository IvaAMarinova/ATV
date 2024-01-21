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
