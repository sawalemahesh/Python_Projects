import requests
from jsonschema import validate


def test_schema_validation():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)
    data = response.json()
    print(data)

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    # Schema validation
    validate(instance=data, schema=schema)