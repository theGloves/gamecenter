from marshmallow import Schema, fields


class CreateRoomSchema(Schema):
    creator_id = fields.Str(required=True)
    
    class Meta:
        strict = True

