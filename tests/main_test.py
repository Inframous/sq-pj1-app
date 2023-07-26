
import pytest 

class TestService:
    def test_greeting(self, client):
        response = client.post('/sayhello', data={'username': 'test_user1'})
        assert response.status_code == 200
        assert b'test_user1' in response.data

        response = client.post('/sayhello', data={'username': 'test_user2'})
        assert response.status_code == 200
        assert b'test_user2' in response.data


class TestDatabase:
    def test_database(self, client):
        response = client.post('/sayhello', data={'username': 'test_user1'})
        assert response.status_code == 200

        response = client.post('/sayhello', data={'username': 'test_user2'})
        assert response.status_code == 200

        response = client.get('/db')
        assert response.status_code == 200
        assert b'test_user1' in response.data
        assert b'test_user2' in response.data