import asyncio
from connectFour import connectFour

def main():
    runconnectFour = connectFour()
    asyncio.run(runconnectFour.run())

asyncio.run(main())