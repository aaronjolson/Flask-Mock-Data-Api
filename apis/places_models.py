from flask_restx import Namespace, fields

api = Namespace(
    'Places Data',
    path='/',
    description='Some place data'
)

place_obj = {
    "latitude": fields.String(
        description="example of a person's name",
        example='38.70734'
        ),
    "longitude": fields.String(
        description="example of a home address",
        example='-77.02303'
        ),
    "placeName": fields.String(
        description="example of a phone number",
        example='Fort Washington'
        ),
    "countryCode": fields.String(
        description="country code",
        example='US'
        ),
    "timezone": fields.String(
        description="timezone",
        example='America/New_York'
        )
}


place_response = api.model(
    'Place-Response', {
        **place_obj
    }
)

places_response = api.model(
    'Places-Response', {
        "places": fields.List(fields.Nested(model=place_response))
    }
)
