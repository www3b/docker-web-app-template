FROM python:3

ENV PYTHONUNBUFFERED=1 \
    POETRY_HOME=/etc/poetry \
    PATH="/etc/poetry/bin:$PATH"

# Create and set the working directory
WORKDIR /app

# copy poetry files to the working directory
COPY ./fastapi/poetry.lock ./fastapi/pyproject.toml /app

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# check taht poetry installed correctly
RUN poetry config virtualenvs.create false && poetry install

# Copy the FastApi project into the container
COPY ./fastapi /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
