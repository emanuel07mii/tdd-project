from fastapi import FastAPI
from store.db.mongo import db_client
from contextlib import asynccontextmanager

from store.core.config import settings
from store.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App()
app.include_router(api_router)


@asynccontextmanager
async def lifespan():
    client = db_client.get()
    db = client.get_database()
    products_collection = db.get_collection("products")

    # garante que não haja conflito ao criar índice
    await products_collection.create_index("name", unique=True)
