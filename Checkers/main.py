import asyncio
from checkersBoard import CheckersBoard

async def main():
    myCheck = CheckersBoard()
    asyncio.run(myCheck.run())

asyncio.run(main())