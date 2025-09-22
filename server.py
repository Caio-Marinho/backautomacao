import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",  # ou "127.0.0.1" para só localhost
        port=5000,
        reload=True  # recarrega automaticamente ao salvar alterações
    )
