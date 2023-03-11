import pytest

from os import environ

from api.models import Blurb
from .utils import current_date

@pytest.mark.freeze_time("2023-03-14 15:09:26")
def test_new_blurb(current_date):
  data = {
    "title": "test note",
    "content": "this is the content of the test note",
    "datetime": current_date
  }

  blurb = Blurb(
    title=data["title"],
    content=data["content"],
    datetime=data["datetime"]
  )

  assert blurb.title == data["title"]
  assert blurb.content == data["content"]
  assert blurb.datetime == data["datetime"]


def test_environ():
  host = environ.get('DB_HOST')
  password = environ.get('DB_PASS')
  user = environ.get('DB_USER')
  db = environ.get('DB_NAME')

  assert host == "dpg-cg6bqdpmbg5ab7k57id0-a.ohio-postgres.render.com"
  assert password == "8fLLDmDIVEKGrKltLwiXdmuWyPCIiWTE"
  assert user == "pfrn"
  assert db == "pfrn"