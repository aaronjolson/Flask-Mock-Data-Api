
def test_place(client):
    assert client.get('/place').status_code == 200


def test_places(client):
    assert client.get('/places').status_code == 200


def test_person(client):
    assert client.get('/person').status_code == 200


def test_people(client):
    assert client.get('/people').status_code == 200
