# Minesweeper Game

This is a simple implementation of the classic Minesweeper game using Python's Tkinter library. The game allows players to explore a grid, revealing cells and avoiding mines.

## How to Play

1. Run the script (`minesweeper.py`).
2. Enter the number of rows, columns, and mines when prompted.
3. Left-click on cells to reveal them.
4. If you reveal a mine, the game is over.
5. The number on a revealed cell indicates the number of adjacent mines.
6. The goal is to reveal all cells without hitting a mine.

## Code Structure

The code is organized into a class `MinesweeperGUI` that handles the game's logic and a function `play_minesweeper_gui` to start the game.

### `MinesweeperGUI` Class

- **Initialization**: Initializes the game with the specified number of rows, columns, and mines.
- **`generate_mines`**: Randomly places mines on the board.
- **`calculate_numbers`**: Calculates the number of adjacent mines for each cell.
- **`create_board`**: Creates the game board with buttons using Tkinter.
- **`reveal_cell`**: Reveals a cell when clicked, handles game over if a mine is revealed, and recursively reveals empty cells.
- **`reveal_empty_cells`**: Recursively reveals adjacent empty cells.
- **`reveal_all`**: Reveals all cells when the game is over.

### `play_minesweeper_gui` Function

- **Tkinter Setup**: Creates the Tkinter window and gets input for the number of rows, columns, and mines.
- **Game Initialization**: Creates an instance of `MinesweeperGUI`.
- **Mainloop**: Enters the Tkinter main loop to run the game.

## Dependencies

- Python 3
- Tkinter (usually included with Python)

## Running the Game

```bash
python minesweeper.py
```
