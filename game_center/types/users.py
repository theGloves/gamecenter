from marshmallow import Schema, fields


class RegistryUserSchema(Schema):
    username = fields.Str(required=True)

    class Meta:
        strict = True
