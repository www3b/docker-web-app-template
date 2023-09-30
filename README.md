# Template for REST web application

To start the app run this commands:

```
docker-compose up -d --build
docker-compose exec fastapi alembic upgrade head
```

Then you can go to [http://localhost:8000/docs](http://localhost:8000/docs)

## Application stack

- FastApi
- Vue 3
- PostgreSQL
- Redis
