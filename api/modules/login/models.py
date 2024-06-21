from peewee import AutoField,CharField
from origin_db import Base

class LoginInfo(Base):
  id = AutoField(primary_key=True)
  user_name = CharField(max_length=20,null=False)
  user_pass = CharField(max_length=24,null=False)
  class Meta:
    table_name = "base_info"

