from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import api_router


app = FastAPI()

app.add_middleware(  
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Cash Machine API"}

app.include_router(api_router)