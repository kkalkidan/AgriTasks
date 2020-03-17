from app import db

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.String(64), primary_key=True)
