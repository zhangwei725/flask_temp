import datetime

from apps.ext import db


class Travel(db.Model):
    travel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True, index=True, nullable=False)
    price = db.Column(db.Numeric(9, 2), default=0.00, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    is_delete = db.Column(db.Boolean, default=0)
    images = db.relationship('Image', backref='travel', lazy='dynamic')


class Image(db.Model):
    img_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    travel_id = db.Column(db.Integer, db.ForeignKey(Travel.travel_id))
