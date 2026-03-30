from fastapi import FastAPI
from planner import create_plan
from orchestrator import execute_plan
from schemas import UserRequest

app = FastAPI()

@app.post("/process")
async def process_request(request: UserRequest):

    user_input = request.user_input

    plan = create_plan(user_input)
    result = await execute_plan(plan)

    return {
        "input": user_input,
        "plan": plan,
        "result": result
    }