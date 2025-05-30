
# FastAPI Function Dispatcher

This FastAPI application exposes a single endpoint `/execute` that analyzes a natural language query, identifies a matching function name, extracts required parameters, and returns a structured JSON response. It acts as a basic NLU (Natural Language Understanding) processor for function dispatching.

## 📁 Project Structure

```
hello/
├── app.py             # FastAPI application entrypoint
├── main.py            # Core logic to parse queries and return function mappings
├── functions.py       # Stub functions representing possible backend calls
├── utils.py           # Helper methods (e.g., regex patterns or matchers)
├── __pycache__/       # Compiled Python files
└── venv/              # Python virtual environment
```

---

## 🚀 Features

- **Natural Language Parsing**: Understands specific patterns in English questions.
- **Function Mapping**: Converts a query into a function name and its JSON arguments.
- **CORS Enabled**: Supports cross-origin GET requests.
- **Modular Codebase**: Clean separation of logic across modules.

---

## 🔧 Setup Instructions

1. **Clone the project** (if not already):

   ```bash
   git clone <your-repo-url>
   cd hello
   ```

2. **Create a virtual environment** (if not created already):

   ```bash
   python -m venv venv
   source venv/Scripts/activate      # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the app** on a custom port (e.g., 8001 to avoid conflicts):

   ```bash
   uvicorn app:app --reload --port 8001
   ```

---

## 🌐 API Usage

### **Endpoint**

```
GET /execute?q=...
```

### **Base URL Example**

```
http://127.0.0.1:8001/execute?q=What is the status of ticket 83742?
```

### **Sample Queries and Expected Responses**

| Query                                                   | Response                                                                                 |
|----------------------------------------------------------|------------------------------------------------------------------------------------------|
| What is the status of ticket 83742?                     | `{ "name": "get_ticket_status", "arguments": "{"ticket_id": 83742}" }`               |
| Schedule a meeting on 2025-06-15 at 14:30 in Room 204.  | `{ "name": "schedule_meeting", "arguments": "{"date": ..., "time": ..., ...}" }`    |
| Bonus details for employee 98298 for 2025               | `{ "name": "calculate_performance_bonus", "arguments": "{"employee_id": ..., ...}" }` |

---

## 🧠 Supported Patterns

The application currently supports the following types of queries:

- **Ticket Status**:  
  _"What is the status of ticket 83742?"_

- **Schedule Meeting**:  
  _"Schedule a meeting on 2025-06-15 at 14:30 in Conference Room 3."_

- **Expense Balance**:  
  _"What is the expense balance for employee 12345?"_

- **Performance Bonus**:  
  _"Bonus details for employee 98298 for 2025"_

- **Office Issue Report**:  
  _"Report issue 102 for the maintenance department"_

---

## 📂 File Descriptions

- **`app.py`**: Initializes the FastAPI app, sets up CORS, and defines the `/execute` endpoint.
- **`main.py`**: Contains the logic to identify and parse queries, returning the correct function call mapping.
- **`functions.py`**: Placeholder module with function definitions for reference.
- **`utils.py`**: Houses helper utilities like regex patterns for query parsing.

---

## ✅ Example Test

```bash
curl "http://127.0.0.1:8001/execute?q=What is the status of ticket 83742?"
```

Expected Response:

```json
{
  "name": "get_ticket_status",
  "arguments": "{"ticket_id": 83742}"
}
```

---

## 📝 Notes

- Be sure to run only one FastAPI app per port at a time.
- This API is designed to be backend-compatible with any UI, chatbot, or automation tool that interprets natural language queries.

---

Let me know if you want me to help with anything else!
