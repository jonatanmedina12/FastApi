from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Inicializamos FastAPI
app = FastAPI()

# Modelo para los datos
class Item(BaseModel):
    nombre: str
    precio: float
    disponible: bool = True

# Lista para almacenar los items (en memoria)
items_db: List[Item] = [
    Item(nombre="Laptop Gaming", precio=1299.99, disponible=True),
    Item(nombre="Monitor 4K", precio=499.99, disponible=True),
    Item(nombre="Teclado Mecánico", precio=89.99, disponible=True),
    Item(nombre="Mouse Gamer", precio=49.99, disponible=False),
    Item(nombre="Auriculares RGB", precio=79.99, disponible=True),
    Item(nombre="Webcam HD", precio=59.99, disponible=True),
    Item(nombre="SSD 1TB", precio=129.99, disponible=True),
    Item(nombre="Tarjeta Gráfica RTX", precio=799.99, disponible=False),
    Item(nombre="RAM 16GB", precio=89.99, disponible=True),
    Item(nombre="Gabinete RGB", precio=149.99, disponible=True)
]
# GET endpoint para obtener todos los items
@app.get("/items")
async def get_items():
    return items_db

# GET endpoint para obtener un item por índice
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        return {"error": "Item no encontrado"}
    return items_db[item_id]

# POST endpoint para crear un nuevo item
@app.post("/items")
async def create_item(item: Item):
    items_db.append(item)
    return {"mensaje": "Item creado", "item": item}

# Para ejecutar la aplicación:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)