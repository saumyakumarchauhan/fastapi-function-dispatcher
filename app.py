from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import re
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/execute")
def execute(q: str = Query(...)):
    # --- Fixed Sample Case ---
    match = re.match(r".*status of ticket (\d+)", q, re.IGNORECASE)
    if match:
        ticket_id = int(match.group(1))
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": ticket_id})
        }

    # --- Schedule meeting ---
    match = re.match(r".*Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+?)\.", q, re.IGNORECASE)
    if match:
        date, time, room = match.groups()
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": date,
                "time": time,
                "meeting_room": room
            })
        }

    # --- Expense balance ---
    match = re.match(r".*expense balance for employee (\d+)", q, re.IGNORECASE)
    if match:
        employee_id = int(match.group(1))
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": employee_id})
        }

    # --- Performance bonus (full sentence) ---
    match = re.match(r".*bonus.*employee (\d+) for (\d{4})", q, re.IGNORECASE)
    if match:
        employee_id, year = match.groups()
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(employee_id),
                "current_year": int(year)
            })
        }

    # --- Performance bonus (short format) ---
    match = re.match(r".*emp\s+(\d+)\s+bonus\s+(\d{4})", q, re.IGNORECASE)
    if match:
        employee_id, year = match.groups()
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(employee_id),
                "current_year": int(year)
            })
        }

    # --- Office issue report ---
    match = re.match(r".*issue (\d+) for the (.+?) department", q, re.IGNORECASE)
    if match:
        issue_code, department = match.groups()
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(issue_code),
                "department": department
            })
        }

    # --- Default fallback ---
    return {"error": "Could not understand the query"}
