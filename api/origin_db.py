from peewee import Model,PostgresqlDatabase
import config

engine= PostgresqlDatabase(config.DB,user=config.USER,host=config.HOST,port=config.PORT,password=config.PASS)

class Base(Model):
  class Meta:
    database = engine

def get_db():
   try:
      engine.connect()
      yield
   finally:
      engine.close()