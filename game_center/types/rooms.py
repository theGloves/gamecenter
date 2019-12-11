from marshmallow import Schema, fields


class CreateRoomSchema(Schema):
    creator_id = fields.Str(required=True)

    class Meta:
        strict = True


class JoinGameSchema(Schema):
    user_id = fields.Str(required=True)
    room_id = fields.Int(required=True)

    class Meta:
        strict = True


class DropChessSchema(Schema):
    user_id = fields.Str(required=True)
    room_id = fields.Int(required=True)
    x = fields.Int(required=True)
    y = fields.Int(required=True)

    class Meta:
        strict = True
