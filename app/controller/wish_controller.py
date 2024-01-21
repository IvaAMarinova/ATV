from app.model.wish import Wish
from app.extensions import db

def add_wish_logic(content):
    new_wish = Wish(content=content)
    db.session.add(new_wish)
    db.session.commit()
    return new_wish

def remove_wish_logic(wish_id):
    wish = Wish.query.get(wish_id)
    if wish:
        db.session.delete(wish)
        db.session.commit()
        return wish
    return None

def get_wish_logic(wish_id):
    return Wish.query.get(wish_id)

def get_all_wishes_logic():
    return Wish.query.all()

def like_wish_logic(wish_id):
    wish = Wish.query.get(wish_id)
    if wish:
        wish.likes += 1
        db.session.commit()
        return wish
    return None
