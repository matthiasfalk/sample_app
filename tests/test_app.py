# Third party modules
import pytest

# First party modules
from sample_app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predictions(client):
    rv = client.get("/predictions")
    assert rv.data == b'Pinging Model Application!!'