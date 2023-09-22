from app import db
from datetime import datetime

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'review': self.review,
            'date_created': self.date_created
        }
