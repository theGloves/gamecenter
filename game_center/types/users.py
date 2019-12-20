from marshmallow import Schema, fields


class RegistryUserSchema(Schema):
    username = fields.Str(required=True)

    class Meta:
        strict = True

class RegistryUserSchema(Schema):
    user_id = fields.Str(required=True)
    score = fields.Int(required=True)

    class Meta:
        strict = True
