# functions.py

def get_ticket_status(ticket_id: int) -> str:
    # Dummy: just return a string
    return f"Status for ticket {ticket_id} is Open."

def schedule_meeting(date: str, time: str, meeting_room: str) -> str:
    return f"Meeting scheduled on {date} at {time} in {meeting_room}."

def get_expense_balance(employee_id: int) -> float:
    return 1234.56  # dummy amount

def calculate_performance_bonus(employee_id: int, current_year: int) -> float:
    return 1000.0  # dummy bonus

def report_office_issue(issue_code: int, department: str) -> str:
    return f"Issue {issue_code} reported for {department}."
