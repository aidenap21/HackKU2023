import asyncio
from checkersBoard import CheckersBoard

def main():
    myCheck = CheckersBoard()
    asyncio.run(myCheck.run())

asyncio.run(main())