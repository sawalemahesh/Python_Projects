import requests

def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200
    print(response.json())


def test_get_single_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

    # Response time in seconds

    assert response.elapsed.total_seconds() <2

    print(response.json())