from fastapi import FastAPI,Query
from enum import Enum
from typing import Union

app = FastAPI()

# http://127.0.0.1:8000/items/?skip=0&limit=10      - In a URL, there are 2 types of parameters in URL - Path Parameter and Query Parameters
# items is PATH PARAMETER
# skip, limit are QUERY PARAMETERS  - comes after "?"

# Command to run is 
# uvicorn <file_name_without.py>:app --reload

# 1) Standard get api
@app.get('/')
async def root():
    return {"message1":"This is FastAPI root URL GET operation response",
    "documentation": "See all URL APIs available in http://127.0.0.1:8000/docs",
    "url2":"/items/<item_id>  Ex: http://127.0.0.1:8000/items/2 ",
    "FastAPI":"Easy to use framework for building APIs in Python. Best part is - Automatic documentation, Automatic URL data conversion & validation. Easy framework rules.",
    "Tutorial":"https://fastapi.tiangolo.com/tutorial/"}

# 2) How to access PATH PARAMETER from URL
@app.get('/items/{item_id}')
async def getItem(item_id: int):
    return {"item_id": item_id,
             "item_name":"You requested for item %s"%item_id}

# 3) Using Enum so that PATH PARAMETER will have to be one of enums
class ItemTypes(str, Enum):
    clothes="clothes"
    food="food"
    electronics="electronics"
    stationary="stationary"

@app.get("/itemtypes/{item_type}")
async def getItemType(item_type: ItemTypes):
    if item_type=="clothes":
        return {"item_type":item_type,"message":"Welcome to clothes section"}
    if item_type=="food":
        return {"item_type":item_type,"message":"Welcome to food section"}
    if item_type=="electronics":
            return {"item_type":item_type,"message":"Welcome to electronics section"}
    if item_type=="stationary":
        return {"item_type":item_type,"message":"Welcome to stationary section"}

# 4) Query parameters and Validation
@app.get("/item/")
async def getItemDetails(itemid: int = 0,location: str = "",itemname:Union[str, None] = Query(default=None, max_length=10)):
    # get details from db
    results = {"itemid":itemid,"location":location,"available":"true","price":"$20"}
    if itemname:
        results.update({"item_name": itemname})
    return results

