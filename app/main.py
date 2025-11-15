from fastapi import FastAPI
from app.schemas import LogEntry, Report
from app.database import save_report, get_reports
from app.detectors import analyze_request

app = FastAPI(title="Secure Request Monitor", version="1.0")

@app.post("/analyze", response_model=Report)
def analyze(entry: LogEntry):
    score, issues = analyze_request(entry)
    report = save_report(entry, score, issues)
    return report

@app.get("/reports", response_model=list[Report])
def reports():
    return get_reports()
