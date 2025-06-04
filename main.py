from fastapi import FastAPI
from routers.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 허용할 도메인 리스트
origins = [
    "https://friendly-lamp-pj9wr9q5vvvghr57g-3000.app.github.dev",  # 플러터 웹 앱 도메인
    "*",  # 개발 편의를 위해 모든 도메인 허용 (배포 전 꼭 제한하세요)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # 허용할 도메인
    allow_credentials=True,
    allow_methods=["*"],             # 모든 HTTP 메서드 허용
    allow_headers=["*"],             # 모든 헤더 허용
)

app.include_router(auth_router)
