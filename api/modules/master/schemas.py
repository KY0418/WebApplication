from pydantic import BaseModel,Field

class LoginDataBase(BaseModel):
  id : int = Field(None)
  user_name: str
  user_pass : str 

class LoginData(BaseModel):
  user_name : str
  user_pass : str