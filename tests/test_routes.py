from app import app
from models import  db
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_get_data(client):
    response = client.get('/get_data?store_name=Shop')
    assert response.status_code == 200
    # 在这里添加更多的断言，验证返回的数据是否符合预期