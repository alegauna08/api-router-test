from fastapi import FastAPI
from routers.clientesRouter import router as routerClientes
from routers.pedidosRouter import router as routerPedidos
from routers.productosRouter import router as routerProductos

app = FastAPI()
app.include_router(routerClientes)
app.include_router(routerProductos)
app.include_router(routerPedidos)