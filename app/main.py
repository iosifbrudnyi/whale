import aiopg
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.leads import router as leads_router
from api.tower import router as tower_router

app = FastAPI(title="API")
app.include_router(leads_router, prefix='/api', tags=["api"])
app.include_router(tower_router, prefix='/api', tags=["api"])


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()