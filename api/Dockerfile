FROM python:3.11-buster

ENV PYTHONNUNBUFFERED=1

WORKDIR /src/api

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

# RUN poetry add uvicorn[standard]

RUN poetry config virtualenvs.in-project true
# RUN poetry config virtualenvs.create false
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]

