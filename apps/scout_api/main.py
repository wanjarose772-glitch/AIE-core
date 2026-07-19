from dotenv import load_dotenv
load_dotenv()
from packages.hawk.hawk import discover_new_tokens
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from packages.intelligence.report import build_intelligence_report
from packages.radar.radar import build_alpha_radar
from packages.history.comparison import compare_snapshots

app = FastAPI(
    title="ASILI Intelligence Engine",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "ASILI Intelligence Engine is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/intel")
def intel():
    return build_intelligence_report()


@app.get("/radar")
def radar():
    return build_alpha_radar()


@app.get("/compare")
def compare():
    return compare_snapshots()
@app.get("/hawk")
def hawk():
    return discover_new_tokens()