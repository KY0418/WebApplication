from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.master import api
import logging

logging.getLogger('uvicorn').setLevel(logging.DEBUG)

app = FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins = ['http://localhost:3030'],#request元を許可する デプロイ前はドメインを入れる
      allow_methods = ["DELETE","POST","GET","PUT"],
      allow_credentials=True,
      allow_headers = ["*"]
  )

app.include_router(api.router)
