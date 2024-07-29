import pytest
from app import app, db
from app.models import Cell, CellData

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_get_cells(client):
    # Add test data
    with app.app_context():
        cell = Cell(cell_id='test', discharge_capacity=2900, nominal_capacity=3000)
        db.session.add(cell)
        db.session.commit()

    response = client.get('/api/cells')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['cell_id'] == 'test'
    assert data[0]['soh'] == (2900 / 3000) * 100

def test_get_cell_data(client):
    # Add test data
    with app.app_context():
        cell = Cell(cell_id='test', discharge_capacity=2900, nominal_capacity=3000)
        db.session.add(cell)
        cell_data = CellData(cell_id='test', time=0, current=1, voltage=3.7, capacity=2900, temperature=25)
        db.session.add(cell_data)
        db.session.commit()

    response = client.get('/api/cell/test')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['time'] == 0
    assert data[0]['current'] == 1
    assert data[0]['voltage'] == 3.7
    assert data[0]['capacity'] == 2900
    assert data[0]['temperature'] == 25
