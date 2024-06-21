from modules.login.schemas import LoginData
from modules.login.models import LoginInfo as LoginTable


async def regist_data(rq_data: LoginData) -> LoginTable:
    login_table = LoginTable.create(**rq_data.model_dump())

    return login_table


async def res_match_data(rq_data: LoginData) -> str | None:
    result = LoginTable.select(LoginTable.user_name).filter(
        (LoginTable.user_name == rq_data.user_name)
        & (LoginTable.user_pass == rq_data.user_pass)
    )
    if not result:
        return None
    else:
        return result[0].user_name
