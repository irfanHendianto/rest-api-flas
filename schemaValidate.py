from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from voluptuous import Optional

class CreateTodoInputs(Inputs):
    json = [JsonSchema({
        'type': 'object',
        'properties': {
            'title': {'type': 'string', 'minLength': 1},
            'description': {'type': 'string', 'minLength': 1}
        },
        'required': ['title', 'description']
    })]
    
class UpdateTodoInputs(Inputs):
    json = [JsonSchema({
        'type': 'object',
        'properties': {
            Optional('title'): {'type': 'string', 'minLength': 1},
            Optional('description'): {'type': 'string', 'minLength': 1}
        }
    })]
