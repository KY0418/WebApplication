from modules.master.schemas import LoginData
from modules.master.models import LoginInfo

async def regist_data(rq_data:LoginData) -> LoginInfo:
  print("2222")
  login_table = LoginInfo.create(**rq_data.model_dump())
  
  return login_table
