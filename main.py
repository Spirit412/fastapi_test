import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from core.db import SessionLocal
from routes import routes

# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)


# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="/static/templates")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, use_colors=True, reload=True)
