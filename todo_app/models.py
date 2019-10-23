from todo_app import db


class TODO(db.Model):
    """Define your table columns here"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(1024))

    def __repr__(self):
        return '<TODO %r>' % self.text