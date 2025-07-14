from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def helloWorld():
    return "Hello world"

@app.get("/about")
def aboutPage():
    return "This is about api"