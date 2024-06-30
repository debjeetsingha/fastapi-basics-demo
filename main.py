from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from random import choice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods= ["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return FileResponse("frontend/index.html")

@app.get("/api/randomname")
async def random_name():
    name_list = ["Debjeet", "Debojit", "Devmalya", "Shaurya", "Ashvini", "Debolina"]
    name = choice(name_list)
    return {"name" : name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)