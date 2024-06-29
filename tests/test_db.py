from app.blueprints.auth.models import User

def test_create_user(client):
    new_user = User(username='testuser', role='usuario', agency='wiwili3')
    assert new_user.username == 'testuser'
    assert new_user.role == 'usuario'
    assert new_user.agency == 'wiwili3'
