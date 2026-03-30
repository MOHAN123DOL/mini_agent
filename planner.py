'''import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_plan(user_input: str):
    prompt = f"""
    Convert the following user request into JSON steps.

    Rules:
    - Use actions: cancel_order, send_email
    - Extract order_id and email
    - Return JSON list only

    Example:
    Input: Cancel my order #1234 and email me at test@example.com
    Output:
    [
      {{"action": "cancel_order", "order_id": "1234"}},
      {{"action": "send_email", "email": "test@example.com"}}
    ]

    User Input: {user_input}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        plan = json.loads(content)
    except:
        plan = []

    return plan'''



import re

def create_plan(user_input: str):
    """
    Mock LLM planner (simulates AI behavior)
    """

    plan = []

    order_match = re.search(r"#?(\d+)", user_input)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", user_input)

    if order_match:
        plan.append({
            "action": "cancel_order",
            "order_id": order_match.group(1)
        })

    if email_match:
        plan.append({
            "action": "send_email",
            "email": email_match.group(0)
        })

    return plan