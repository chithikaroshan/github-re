# FastAPI PostgreSQL Backend Service

## 📌 Problem Understanding & Assumptions

### 🔍 Interpretation
The goal of this project is to build a robust REST API using FastAPI and PostgreSQL that demonstrates:
- Proper state management using a relational database
- Integration with an external API
- Strict request and response validation
- Clean architecture and testing practices

The service implements exactly four REST endpoints: POST, GET, PUT, and DELETE.

---

### 🎯 Use Case
AI-Powered Task Management Service

Users can create tasks, which are enriched using an external API (for example, an AI summary service), and then stored and managed in a PostgreSQL database.

---

### 📌 Assumptions
- User authentication and authorization are out of scope
- External API availability is not guaranteed and may fail
- API keys are stored securely using environment variables
- PostgreSQL is available locally or via Docker
- Each task is uniquely identified by a UUID

---

## 🏗 Design Decisions

### 🗄 Database Schema

Table: tasks

| Column       | Type        | Description                    |
|--------------|-------------|--------------------------------|
| id           | UUID (PK)   | Unique task identifier         |
| title        | VARCHAR     | Task title                     |
| description  | TEXT        | Task description               |
| ai_summary   | TEXT        | Summary from external API      |
| status       | VARCHAR     | pending / completed            |
| created_at   | TIMESTAMP   | Task creation time             |

---

### 📁 Project Structure

app/
 ├── main.py
 ├── api/routes.py
 ├── models/task.py
 ├── schemas/task_schema.py
 ├── services/external_api.py
 ├── db/session.py
 └── tests/

Architecture style: Layered / Clean Architecture

---

### ✅ Validation Logic
- Pydantic models used for request and response validation
- Business rules enforced beyond basic type checking

---

### 🌐 External API Design
- External API used to generate task summaries
- API key-based authentication
- Timeout and fallback handling implemented

---

## 🔄 Solution Approach

1. POST /tasks – Create a task and enrich it using an external API
2. GET /tasks/{id} – Retrieve a task by ID
3. PUT /tasks/{id} – Update an existing task
4. DELETE /tasks/{id} – Delete a task

---

## 🚨 Error Handling Strategy
- Global exception handlers in FastAPI
- Graceful handling of database and external API failures
- Proper HTTP status codes returned

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.10+
- PostgreSQL

### Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables
DATABASE_URL=postgresql://user:password@localhost:5432/tasksdb
EXTERNAL_API_KEY=your_api_key_here

### Run
```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing
- Pytest for unit and integration tests
- HTTPX used for API testing

Run tests:
```bash
pytest
```

---

## 👤 Author
Python Backend Engineer – Take Home Assessment
