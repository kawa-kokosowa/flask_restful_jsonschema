# `flask_restful_jsonschema`

Add the `@validate_json` decorator and schema class constant to
`flask_restful.Resource` methods (post, get, etc.) in order to validate
requests meet the `jsonschema`.


```python
from flask_restful_jsonschema import validate_json


class Users(flask_restful.Resource):
    SCHEMA_POST = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "password": {"type": "string"},
        },
        "required": ["email", "password"],
    }
    SCHEMA_PUT = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "password": {"type": "string"},
        },
    }
    SCHEMA_GET = {
        "type": "object",
        "properties": {
            "email": {"type": "string"},
        },
        "required": ["email"],
    }

    @validate_json
    def post(self, json_request):
        pass

    @validate_json
    def put(self, json_request):
        pass

    @validate_json
    def get(self, json_request):
        pass
```
