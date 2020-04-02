'''
用户指南-额外模型
'''

from typing import Union, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = 'car'

class PlaneItem(BaseItem):
    type = 'plane'
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "size": 5
    },
}


'''

Union 或 anyOf

        您可以将响应声明为两种类型的联合，这意味着响应将是两种类型中的任何一种。

        它将在OpenAPI中使用anyOf进行定义
'''
'''可以根据响应模型 补全响应结构体'''

@app.get('/items/{item_id}', response_model = Union[PlaneItem, CarItem])
def read_item(item_id: str):
    return items[item_id]


class Item_list(BaseModel):
    name: str
    description: str


'''模型列表'''
items_list = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get('/item_list/', response_model=List[Item_list])

def read_item_list():
    return items


'''用任意字典响应'''

@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}