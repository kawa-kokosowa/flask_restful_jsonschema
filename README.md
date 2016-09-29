# `flask_restful_jsonschema`

[![PyPI Version](https://img.shields.io/pypi/v/flask_restful_jsonschema.svg?style=flat-square)](https://pypi.python.org/pypi/flask_restful_jsonschema/)

Add the `@validate_json` decorator and schema class constant to
`flask_restful.Resource` methods (post, get, etc.) in order to validate
requests meet the `jsonschema`.

Ensure JSON request matches schema specified in the class the wrapped method
belongs to, provide that valid JSON to the method, or abort 400 with the
validation error message.


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
