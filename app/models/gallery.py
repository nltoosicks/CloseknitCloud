from app import db
from datetime import datetime

gallery_members = db.Table('gallery_members',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('gallery_id', db.Integer, db.ForeignKey('gallery.id'), primary_key=True)
)

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    owner = db.relationship('User', backref='owned_galleries', foreign_keys=[owner_id])
    members = db.relationship('User', secondary=gallery_members, lazy='subquery',
                              backref=db.backref('galleries', lazy=True))

    def __repr__(self):
        return f'<Gallery {self.name}>'
