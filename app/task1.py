from fastapi import FastAPI, Request
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
async def get_time_service(request: Request):
    
    timestamp = datetime.now().isoformat()

    
    ip = request.client.host

    
    return {
        "timestamp": timestamp,
        "ip": ip
    }
