from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.params import Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Visitor(BaseModel):
    client_ip: str
    location: str
    greeting: str
    
    
@app.get("/api/hello")
def hello(visitor_name: Optional[str] = Query(...)):
    client_ip = "127.0.0.1"
    location = "Lagos"
    temperature = 11
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degree celcius in {location}"
    return JSONResponse(content= {"client_ip": client_ip,"location":location, "greeting":greeting}, media_type="application/json")
