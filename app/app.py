from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.controller.wish_controller import add_wish, remove_wish, get_wish, get_all_wishes, like_wish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.route('/add_wish', methods=['POST'])(add_wish)
app.route('/wishes/<int:wish_id>', methods=['DELETE'])(remove_wish)
app.route('/wishes/<int:wish_id>', methods=['GET'])(get_wish)
app.route('/wishes', methods=['GET'])(get_all_wishes)
app.route('/wishes/<int:wish_id>/like', methods=['POST'])(like_wish)


if __name__ == '__main__':
    with app.app_context():
        test_wish1 = Wish(content='Test Wish aaaaaaaaa')
        test_wish2 = Wish(content='Test Wish bbbbbbbbbb')
        db.session.add_all([test_wish1, test_wish2])
        db.session.commit()

        print('\nGetting all wishes')
        response, _ = get_all_wishes()
        wishes_data = response.get_json()
        for wish in wishes_data:
            print(f'Wish ID: {wish["id"]}, Content: "{wish["content"]}", Timestamp: {wish["timestamp"]}, Likes: {wish["likes"]}')

    app.run(debug=True)