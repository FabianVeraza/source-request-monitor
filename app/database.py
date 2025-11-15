import sqlite3
from app.schemas import LogEntry, Report

conn = sqlite3.connect("monitor.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    method TEXT,
    path TEXT,
    user_agent TEXT,
    score INTEGER,
    issues TEXT
)
""")
conn.commit()

def save_report(entry: LogEntry, score: int, issues: list[str]):
    cursor.execute("""
        INSERT INTO reports (ip, method, path, user_agent, score, issues)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (entry.ip, entry.method, entry.path, entry.user_agent, score, ",".join(issues)))
    
    conn.commit()
    return Report(
        ip=entry.ip,
        method=entry.method,
        path=entry.path,
        user_agent=entry.user_agent,
        score=score,
        issues=issues
    )

def get_reports():
    cursor.execute("SELECT ip, method, path, user_agent, score, issues FROM reports")
    rows = cursor.fetchall()
    
    return [
        Report(
            ip=row[0],
            method=row[1],
            path=row[2],
            user_agent=row[3],
            score=row[4],
            issues=row[5].split(",") if row[5] else []
        )
        for row in rows
    ]
