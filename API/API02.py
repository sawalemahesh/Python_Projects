import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "My Test Post",
        "body": "This is a sample post",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    # Convert response to JSON
    data = response.json()
    print(data)

    # Correct assertion
    assert data["title"] == "My Test Post"