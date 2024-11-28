from fastapi import FastAPI
import uvicorn

import handlers


app = FastAPI()

app.include_router(router=handlers.router)


if __name__ == '__main__':
    uvicorn.run(app)
