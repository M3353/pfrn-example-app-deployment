from os import environ, path
from dotenv import load_dotenv

HOST = environ.get('DB_HOST')
PASS = environ.get('DB_PASS')
USER = environ.get('DB_USER')
NAME = environ.get('DB_NAME')


class Config:
  SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(USER, PASS, HOST, NAME)
  # SQLALCHEMY_DATABASE_URI = "postgresql://pfrn:8fLLDmDIVEKGrKltLwiXdmuWyPCIiWTE@dpg-cg6bqdpmbg5ab7k57id0-a.ohio-postgres.render.com/pfrn"
  