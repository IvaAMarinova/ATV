from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.controller.wish_controller import add_wish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.route('/add_wish', methods=['POST'])(add_wish)

if __name__ == '__main__':
    with app.app_context():
        new_wish = Wish(content='Test Wish')
        db.session.add(new_wish)
        db.session.commit()

        wish = Wish.query.first()
        print(wish.content)

    app.run(debug=True)
