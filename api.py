from unmask import unmasker
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str


@app.get("/")
async def root():
    return {'message':
            "С помощью рассматриваемой модели выполняется "
            "заполнение пропущенного слова на наиболее подходящее. "
            "В качестве входных данных принимается предложение "
            "с помеченным <mask> пропущенным словом."
            }


@app.post('/unmask/')
async def unmask(item: Item): 
    return unmasker(item.text)
