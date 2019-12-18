from .. import db


class Service(db.Model):
    __tablename__ = "gc_service"

    id = db.Column("service_id", db.Integer, primary_key=True)
    name = db.Column("service_name", db.String(255))
    type = db.Column("service_type", db.String(255))
    url = db.Column("service_url", db.String(255))
    desc= db.Column("service_description", db.String(255))
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "url": self.url,
            "desc": self.desc
        }
