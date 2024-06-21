from fastapi import APIRouter, HTTPException, Depends
from modules.login.models import LoginInfo
from modules.login.schemas import LoginData, LoginDataBase
from modules.login.service import regist_data, res_match_data
from peewee import PostgresqlDatabase

# import config
# from origin_db import get_db

router = APIRouter()

# engine= PostgresqlDatabase(database=config.DB,user=config.USER,host=config.HOST,port=config.PORT,password=config.PASS)


@router.post("/signup", response_model=LoginDataBase)
async def regist(rq_data: LoginData):
    result = await regist_data(rq_data)
    if result is None:
        raise HTTPException(status_code=404, detail="Failed to Regist Data")
    return result


@router.post("/signin", response_model=str | None)
async def login(rq_data: LoginData):
    result = await res_match_data(rq_data)
    if result == None:
        raise HTTPException(status_code=404, detail="Not Found Your Data")
    return result


# poetry addしたら　poetry install しないと環境に反映されない?
