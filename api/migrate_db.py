from peewee import PostgresqlDatabase
import config
from modules.master.models import LoginInfo

engine= PostgresqlDatabase(database=config.DB,user=config.USER,host=config.HOST,port=config.PORT,password=config.PASS)

def reset_database():
  engine.drop_tables([LoginInfo],cascade="CASCADE")
  engine.create_tables([LoginInfo])

if __name__ == "__main__":
  engine.connect()
  reset_database()
  engine.close()