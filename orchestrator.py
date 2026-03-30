from tools.orders import cancel_order
from tools.email import send_email

async def execute_plan(plan):
    results = []

    for step in plan:
        action = step["action"]

        
        if action == "cancel_order":
            result = await cancel_order(step["order_id"])

            
            if result["status"] == "failed":
                return {
                    "status": "error",
                    "message": "Order cancellation failed",
                    "details": result
                }

            results.append(result)

        elif action == "send_email":
            result = await send_email(
                step["email"],
                "Your order has been cancelled successfully"
            )
            results.append(result)

    return {
        "status": "success",
        "steps": results
    }