from app.extensions import db
import datetime

class Wish(db.Model):
    __tablename__ = 'wishes'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Wish %r>' % self.content
