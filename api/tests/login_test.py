import pytest
from modules.login.models import LoginInfo
from peewee import PostgresqlDatabase
from modules.login.schemas import LoginData
from modules.login.service import res_match_data, regist_data
import config


engine = PostgresqlDatabase(
    config.DB,
    user=config.USER,
    host=config.HOST,
    port=config.PORT,
    password=config.PASS,
)


@pytest.fixture
def generate_and_initialize():
    test_data = [
        LoginData(user_name="testman1", user_pass="passwordtest33333"),
        LoginData(user_name="testman2", user_pass="agdddr35"),
    ]
    engine.drop_tables([LoginInfo])
    engine.create_tables([LoginInfo])
    for data in test_data:
        LoginInfo.create(**data.model_dump())
    return test_data


@pytest.fixture
def generate_test_data():
    test_data = [
        LoginData(user_name="testman1", user_pass="passwordtest33333"),
        LoginData(user_name="testman2", user_pass="agdddr35"),
    ]
    return test_data


# データを正しく判定できるかどうか


@pytest.mark.asyncio
async def test_login(generate_and_initialize):
    test = generate_and_initialize
    validate_data = await res_match_data(test[0])
    assert validate_data == test[0].user_name
    assert validate_data != test[1].user_name


# データベースに登録できているかどうか
@pytest.mark.usefixtures("generate_test_data")
@pytest.mark.asyncio
async def test_regist(generate_test_data):
    test = generate_test_data
    validate_data = []
    for data in test:
        provide_data = await regist_data(data)
        validate_data.append(
            LoginData(
                user_name=provide_data.user_name, user_pass=provide_data.user_pass
            )
        )
    assert validate_data[0] == test[0]
    assert validate_data[1] == test[1]
