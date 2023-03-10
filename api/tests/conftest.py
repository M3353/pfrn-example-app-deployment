import pytest

from api import db, create_app

@pytest.fixture()
def app():
  app = create_app()

  # teardown
  with app.app_context():
    db.drop_all()
    
  # setup
  with app.app_context():
    db.create_all()

  yield app

@pytest.fixture()
def client(app):
  return app.test_client()

