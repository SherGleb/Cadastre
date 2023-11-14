import time

from fastapi import FastAPI, Depends, HTTPException

from src.database import get_async_session
from src.cadastre_app.schemas import QueryCrete
from sqlalchemy.ext.asyncio import AsyncSession
from src.cadastre_app.models import query
from sqlalchemy import select, insert
from fastapi.responses import RedirectResponse
import random
import starlette.status as status

app = FastAPI()


@app.get('/ping')
def hello():
    try:
        return {"status": "Сервер запущен"}
    except Exception:
        print({"status": "Внутренняя ошибка сервера"})


@app.post('/query')
async def add_query(new_query: QueryCrete, session: AsyncSession = Depends(get_async_session)):
    try:
        time.sleep(random.randint(1, 5))
        result = random.choice((True, False))
        stmt = insert(query).values(**new_query.model_dump(), result=result)
        await session.execute(stmt)
        await session.commit()
        return RedirectResponse(
            f'/result/{result}',
            status_code=status.HTTP_302_FOUND)
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@app.get('/result/{result}')
def add_query(result: bool):
    return result


@app.get('/history')
async def add_query(session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(query)
        result = await session.execute(stmt)
        return result.mappings().all()
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
