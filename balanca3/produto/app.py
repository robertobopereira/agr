from fastapi import FastAPI

app = FastAPI(title="Produto Service")

@app.get("/")
def root():
    return {"service": "produto", "message": "bem-vindo"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/produtos/{sku}")
def get_produto(sku: str):
    return {"sku": sku, "descricao": f"Produto {sku}"}
