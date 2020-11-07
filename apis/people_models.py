from flask_restx import Namespace, fields

api = Namespace(
    'People Data',
    path='/',
    description='Some people data'
)

person_obj = {
    "name": fields.String(
        description="example of a person's name",
        example='Mike Jones'
        ),
    "address": fields.String(
        description="example of a home address",
        example='75639 Kathryn Valleys Apt. 129 Brooksshire, MD 00693'
        ),
    "phone": fields.String(
        description="example of a phone number",
        example='800.123.4567x098'
        )}


person_response = api.model(
    'Person-Response', {
        **person_obj
    }
)

people_response = api.model(
    'People-Response', {
        "people": fields.List(fields.Nested(model=person_response))
    }
)
