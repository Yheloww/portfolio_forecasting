from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    """"""
    return print('test')

@app.get("/item")
