from .. import db


class User(db.Model):
    __tablename__ = "gc_user"

    id = db.Column("id", db.Integer, primary_key=True)
    uid = db.Column("uid", db.String(255), unique=True)
    username = db.Column("username", db.String(255))
    
    def to_dict(self):
        return {
            "id": self.uid,
            "username": self.username
        }
