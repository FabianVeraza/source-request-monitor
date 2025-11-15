from pydantic import BaseModel

class LogEntry(BaseModel):
    ip: str
    method: str
    path: str
    user_agent: str

class Report(BaseModel):
    ip: str
    method: str
    path: str
    user_agent: str
    score: int
    issues: list[str]
