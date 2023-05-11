import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.crystal import Crystal


@pytest.fixture
def app():
    app = create_app(test_config = True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def make_two_crystals(app):
    crystal_1 = Crystal(
        name="pearl",
        color="white",
        powers="pretty power"
    )

    crystal_2 = Crystal(
        name="Garnet",
        color="red",
        powers="Awesomeness"
    )

    db.session.add_all([crystal_1, crystal_2])
    db.session.comit()

  



