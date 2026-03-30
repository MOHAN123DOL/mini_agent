 Mini Agent Orchestrator

 Overview
This project implements a lightweight agentic workflow system using FastAPI.

It processes natural language user requests and executes actions using a structured pipeline:
Planner -- Orchestrator -- Tools.

 Features
 Accepts natural language input
 Converts input into structured actions (Planner)
 Executes actions asynchronously (Orchestrator)
 Simulates real-world failures (20% failure rate)
 Implements guardrails (stops execution on failure)


Architecture

User Input  
   ↓  
Planner (create_plan)  
   ↓  
Orchestrator (execute_plan)  
   ↓  
Tools (cancel_order, send_email)  
   ↓  
Response  



 Components

1. Planner
- Converts user input into structured JSON actions
- Implemented using a mock LLM (regex-based)

2. Orchestrator
- Executes actions dynamically
- Handles failures and controls workflow

3. Tools
- `cancel_order` → simulates order cancellation (with failure rate)
- `send_email` → simulates email sending


 Tech Stack
- Python
- FastAPI
- AsyncIO
- Pydantic

 How to Run

--bash
git clone <https://github.com/MOHAN123DOL/mini_agent>
cd mini-agent

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload --port 5000