from flask import Flask
from app.extensions import db
from app.model.wish import Wish
from app.view.wish_view import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the Blueprint
app.register_blueprint(views)

if __name__ == '__main__':
    with app.app_context():
        # Create a test client to simulate requests
        test_client = app.test_client()

        # Test adding a new wish
        test_content = 'Sample Wish Content'
        response = test_client.post('/add_wish', json={'content': test_content})
        
        if response.status_code == 201:
            print("Wish added successfully.")
            added_wish = Wish.query.filter_by(content=test_content).first()
            if added_wish:
                print(f"Wish ID: {added_wish.id}, Content: '{added_wish.content}'")
        else:
            print("Failed to add wish.")

    app.run(debug=True)
