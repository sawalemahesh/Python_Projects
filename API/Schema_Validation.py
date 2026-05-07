import requests


def test_schema_validation_basic():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)
    data = response.json()
    print(data)

    # Check keys exist
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    # Check data types
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)