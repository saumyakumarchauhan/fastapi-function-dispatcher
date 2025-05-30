# utils.py
import re
import json
from typing import Dict, Optional

def parse_query(q: str) -> Optional[dict]:
    """
    Parse the input query q and return:
    {
      "name": function_name,
      "arguments": json.dumps({param_name: param_value, ...})
    }
    or None if no match.
    """

    # 1. Ticket status
    m = re.match(r"What is the status of ticket (\d+)\?", q, re.I)
    if m:
        ticket_id = int(m.group(1))
        return {"name": "get_ticket_status", "arguments": json.dumps({"ticket_id": ticket_id})}

    # 2. Schedule meeting
    m = re.match(r"Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (Room [A-Z])\.", q, re.I)
    if m:
        date, time, room = m.group(1), m.group(2), m.group(3)
        return {"name": "schedule_meeting", "arguments": json.dumps({
            "date": date, "time": time, "meeting_room": room
        })}

    # 3. Expense balance
    m = re.match(r"Show my expense balance for employee (\d+)\.", q, re.I)
    if m:
        employee_id = int(m.group(1))
        return {"name": "get_expense_balance", "arguments": json.dumps({"employee_id": employee_id})}

    # 4. Performance bonus
    m = re.match(r"Calculate performance bonus for employee (\d+) for (\d{4})\.", q, re.I)
    if m:
        employee_id = int(m.group(1))
        current_year = int(m.group(2))
        return {"name": "calculate_performance_bonus", "arguments": json.dumps({
            "employee_id": employee_id, "current_year": current_year
        })}

    # 5. Report office issue
    m = re.match(r"Report office issue (\d+) for the (.+) department\.", q, re.I)
    if m:
        issue_code = int(m.group(1))
        department = m.group(2)
        return {"name": "report_office_issue", "arguments": json.dumps({
            "issue_code": issue_code, "department": department
        })}

    return None
