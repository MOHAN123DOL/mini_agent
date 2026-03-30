import asyncio
import random

async def cancel_order(order_id: str):
    await asyncio.sleep(1)

    if random.random() < 0.2:
        return {"status": "failed", "order_id": order_id}

    return {"status": "success", "order_id": order_id}