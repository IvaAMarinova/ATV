from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.controller.wish_controller import add_wish, remove_wish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.route('/add_wish', methods=['POST'])(add_wish)
app.route('/wishes/<int:wish_id>', methods=['DELETE'])(remove_wish)

if __name__ == '__main__':
    with app.app_context():
        test_wish = Wish(content='Test Wish')
        db.session.add(test_wish)
        db.session.commit()

        remove_wish(test_wish.id)

        deleted_wish = Wish.query.get(test_wish.id)
        if deleted_wish is None:
            print(f'Wish with ID {test_wish.id} successfully removed.')
        else:
            print(f'Wish with ID {test_wish.id} was not removed.')

    app.run(debug=True)