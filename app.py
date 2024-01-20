from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iva123@localhost:3307/wishes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Wish(db.Model):
    __tablename__ = 'wishes'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Wish %r>' % self.content

if __name__ == '__main__':
    with app.app_context():

        new_wish = Wish(content='Test Wish')
        db.session.add(new_wish)
        db.session.commit()

        wish = Wish.query.first()
        print(wish.content)

    app.run(debug=True)
