from fastapi import FastAPI
from routers.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://friendly-lamp-pj9wr9q5vvvghr57g-3000.app.github.dev/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
