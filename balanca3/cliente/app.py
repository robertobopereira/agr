from fastapi import FastAPI

app = FastAPI(title="Cliente Service")

@app.get("/")
def root():
    return {"service": "cliente", "message": "bem-vindo"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/clientes/{id}")
def get_cliente(id: int):
    return {"id": id, "nome": f"Cliente {id}"}
