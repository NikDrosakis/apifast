from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse
router = APIRouter()
from fastapi.encoders import jsonable_encoder
# import uvicorn
from models.maria import Book, insert, fetchall, update, fetch, delete


# Load variables from .env file into environment

app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>apiFAST v.1.0</h1>
    </body>
</html>
"""
@router.get("/")
async def root():
    return HTMLResponse(html)

tables = ['cat', 'globs', 'media']
table = "globs"


@router.get("/{table}/")
async def get_all_items():
    res = fetchall(table)
    return jsonable_encoder(res)


@router.get("/{table}/{id}")
async def get_one_item(table_id):
    res = fetch(table_id)
    return jsonable_encoder(res)


@router.post("/{table}/")
async def create_book_endpoint(book: Book):
 table_id=insert(book)
 return jsonable_encoder({"message": f"Book created {table_id}"})


@router.put('/{table}/{id}')
async def update_book(table_id, book: Book):
    res = update(table_id, book)
    return jsonable_encoder({"message": f"Updated book {res}"})


@router.delete('/{table}/{id}')
async def delete_book(table_id):
    res = delete(table_id)
    return jsonable_encoder({"message": f"Deleted book {res}"})

# uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")

app.include_router(router)