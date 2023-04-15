import asyncio
from ticTacToe import TicTacToe

def main():
    runTicTacToe = TicTacToe()
    asyncio.run(runTicTacToe.run())

asyncio.run(main())