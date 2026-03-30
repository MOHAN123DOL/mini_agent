import asyncio

async def send_email(email: str, message: str):
    await asyncio.sleep(1)

    return {
        "status": "sent",
        "email": email,
        "message": message
    }