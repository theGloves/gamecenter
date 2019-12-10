from marshmallow import Schema, fields


class RegistryServiceSchema(Schema):
    service_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    service_url = fields.Str(required=True)
    service_desc = fields.Str()

    class Meta:
        strict = True


class RequestServiceSchema(Schema):
    server_data = fields.Dict(required=True)
    service_callback = fields.Str(required=True)

    class Meta:
        strict = True
