from datetime import datetime

from . import db


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    images = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    added_by = db.Column(db.String(64))

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text,
            source=self.source,
            images=self.images,
            timestamp=self.timestamp,
            added_by=self.added_by,
        )

    def from_dict(self, data):
        for field in ['title', 'text', 'source', 'images', 'added_by']:
            if field in data:
                setattr(self, field, data[field])