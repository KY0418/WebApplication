from fastapi import APIRouter,HTTPException,Depends
from modules.master.models import LoginInfo
from modules.master.schemas import LoginData,LoginDataBase
from modules.master.service import regist_data
from peewee import PostgresqlDatabase
# import config 
# from origin_db import get_db

router = APIRouter()

# engine= PostgresqlDatabase(database=config.DB,user=config.USER,host=config.HOST,port=config.PORT,password=config.PASS)


@router.post("/signup",response_model=LoginDataBase)
async def regist(rq_data:LoginData):
    print(rq_data)
    result = await regist_data(rq_data)
    if result is None:
        HTTPException(status_code=404,detail="Failed to Regist Data")
    return result

# poetry addしたら　poetry install しないと環境に反映されない?