from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.controller.wish_controller import add_wish, remove_wish, get_wish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.route('/add_wish', methods=['POST'])(add_wish)
app.route('/wishes/<int:wish_id>', methods=['DELETE'])(remove_wish)
app.route('/wishes/<int:wish_id>', methods=['GET'])(get_wish)

if __name__ == '__main__':
    with app.app_context():
        test_wish1 = Wish(content='Test Wish aaaaaaaaa')
        test_wish2 = Wish(content='Test Wish bbbbbbbbbb')
        db.session.add_all([test_wish1, test_wish2])
        db.session.commit()

        wish_id_to_get = test_wish1.id
        print(f'\nGetting Wish with ID: {wish_id_to_get}')
        response, _ = get_wish(wish_id_to_get)
        wish_data = response.get_json()
        print(f'Wish ID: {wish_data["id"]}, Content: "{wish_data["content"]}", Timestamp: {wish_data["timestamp"]}, Likes: {wish_data["likes"]}')

    app.run(debug=True)