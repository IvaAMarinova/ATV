from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.view.wish_view import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with Flask App
db.init_app(app)

with app.app_context():
    # Create tables
    db.create_all()

app.register_blueprint(views)

if __name__ == '__main__':
    with app.app_context():
        test_client = app.test_client()

        test_content = 'New wish'
        response = test_client.post('/add_wish', json={'content': test_content})
        print(f"Add Wish Response: {response.get_json()}")
        
        if response.status_code == 201:
            added_wish = Wish.query.filter_by(content=test_content).first()
            print(f"Wish ID: {added_wish.id}, Content: '{added_wish.content}'")

            response = test_client.post(f'/wishes/{added_wish.id}/like')
            print(f"Like Wish Response: {response.get_json()}")

            response = test_client.get(f'/wishes/{added_wish.id}')
            print(f"Get Specific Wish Response: {response.get_json()}")

            response = test_client.delete(f'/wishes/{added_wish.id}')
            print(f"Remove Wish Response: {response.get_json()}")

        response = test_client.get('/wishes')
        wishes_data = response.get_json()

        print("Get All Wishes Response:")
        for wish in wishes_data:
            print(f"Wish ID: {wish['id']}, Content: '{wish['content']}', Timestamp: {wish['timestamp']}, Likes: {wish['likes']}")

        response = test_client.delete('/wishes')
        print(f"Remove All Wishes Response: {response.get_json()}")

        test_content = 'New wish'
        response = test_client.post('/add_wish', json={'content': test_content})
        print(f"Add Wish Response: {response.get_json()}")

        response = test_client.get('/wishes')
        wishes_data = response.get_json()

        print("Get All Wishes Response:")
        for wish in wishes_data:
            print(f"Wish ID: {wish['id']}, Content: '{wish['content']}', Timestamp: {wish['timestamp']}, Likes: {wish['likes']}")

    app.run(debug=True)
