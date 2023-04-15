import asyncio
from ticTacToe import TicTacToe

async def main():
    while True:
        runTicTacToe = TicTacToe()
        runTicTacToe.run()
        await asyncio.sleep(0)

asyncio.run(main())