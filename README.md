# Secure Request Monitor 🔐

A lightweight FastAPI-based backend that analyzes HTTP requests and detects
potential security risks such as SQL Injection, XSS, and brute-force attempts.

## 🚀 Features
- FastAPI + Pydantic
- SQL Injection pattern detection
- XSS detection
- Risk scoring (0–100)
- SQLite local storage
- Swagger UI included

## 📡 Endpoints

### POST /analyze
Analyze a request log.
```json
{
  "ip": "127.0.0.1",
  "method": "GET",
  "path": "/login?username=admin'--",
  "user_agent": "Mozilla/5.0"
}
