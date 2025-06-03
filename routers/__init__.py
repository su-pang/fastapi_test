# from .user import router as user_router
# from .post import router as post_router
# from .comment import router as comment_router
from .auth_router import router as auth_router

__all__ = ["auth_router"]
