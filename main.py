from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Coucou"}

@app.get("/test")
def test():
    return {"message": "Ceci est un test"}