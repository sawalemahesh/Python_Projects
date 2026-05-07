import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200


def test_get_users_response_time():
    response = requests.get(f"{BASE_URL}/users")

    assert response.elapsed.total_seconds() < 2


def test_get_users_data_type():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    assert isinstance(data, list)


def test_user_email_validation():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    for user in data:
        assert '@' in user['email']


def test_required_keys_present():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    required_keys = ["id", "name", "username", "email"]

    for user in data:
        for key in required_keys:
            assert key in user

def test_users():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    assert 'Kulas Light' in data[0]['address']["street"]