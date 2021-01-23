"""
    main.py : Main app file
"""

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware 
import schemas
from routes.test import router as TestRouter
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

app = FastAPI()

app.include_router(TestRouter, tags = ["Test"], prefix = "/api/v1/test")

# Remove if you are not requiring any template.
# Mount the static files dir
app.mount(
    "/static", 
    StaticFiles(directory = "static"),
    name = "static"
)

# Templates using Jinja2 Templating engine
## DOCUMENTATION REFERENCE :- https://fastapi.tiangolo.com/advanced/templates/
templates = Jinja2Templates(directory = "templates")

# Adding the route to render index.html template
@app.get("/", response_class = HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})

# Adding CORS middleware to the app to handle Cross-Origin resource sharing 
## DOCUMENTATION REFERENCE :- https://fastapi.tiangolo.com/tutorial/cors/
# Add all origins to this list or set origins = ["*"] to allow all
origins = [
    "http://localhost:8000",
]

# Adding the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler
## DOCUMENTATION REFERENCE :- https://fastapi.tiangolo.com/tutorial/handling-errors/
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({
            "message": "An error occurred",
            "loc" : exc.errors()[0]["loc"],
            "detail": exc.errors()[0]["msg"]
        }),
    )

# Run the app via uvicorn server on PORT 8000
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
