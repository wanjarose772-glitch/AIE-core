from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.discovery_service import DiscoveryService

app = FastAPI(
    title="AIE API",
    version="1.0.0",
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

discovery = DiscoveryService()


@app.get("/")
def home():
    return {
        "status": "online",
        "name": "AIE",
        "version": "1.0.0",
    }


@app.get("/scan")
def scan():
    return discovery.intel()


@app.get("/intel")
def intel():
    return discovery.intel()


@app.get("/hawk")
def hawk():

    tokens = discovery.intel()

    return tokens[:10]