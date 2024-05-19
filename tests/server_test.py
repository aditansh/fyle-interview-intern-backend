def test_base_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200

    status = response.json['status']
    assert status == 'ready'


def test_404(client):
    response = client.get('/non-existent-endpoint')
    assert response.status_code == 404

    error = response.json['error']
    assert error == 'NotFound'