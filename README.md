# Snake Game 🐍

A simple Snake game implemented in Python using the built-in `turtle` module.  
This project was created while learning Python and demonstrates basic game logic,
object-oriented design, and keyboard interaction using Turtle graphics.

---

## Features

- Two play modes:
  - **Easy** – snake wraps around screen edges
  - **Hard** – hitting the wall ends the game
- Score tracking
- Occasional **big food** worth double points
- Snake speed increases as it grows
- Self-collision detection
- Modular OOP-based design

---

## Requirements

- Python **3.x** (3.8+ recommended)
- Uses only the Python standard library (`turtle`)
- No external dependencies

---

## How to Run

From the project directory:

```bash
python3 main.py
```

You will be prompted to choose a mode:

- Enter **1** → Easy (wrap-around)
- Enter **2** → Hard (walls enabled)

### Notes

- Cancelling the numeric input dialog may prevent the game from starting.
- On Linux, make sure you are running in a GUI environment (X server required).

---

## Controls

- **Up Arrow** – Move up
- **Down Arrow** – Move down
- **Left Arrow** – Move left
- **Right Arrow** – Move right
- Close the window or click after _Game Over_ to exit

---

## Gameplay Details

### Food

- **Normal food**: worth **1 point**
- **Big food**:

  - Appears randomly (~1 in 3 chance)
  - Worth **2 points**

Food collision occurs when the snake head is within ~15 pixels of the food.

### Speed Scaling

The snake speeds up as it grows:

- Length < 10
  `delay = 0.2 - (length / 100)`

- 10 ≤ Length < 20
  `delay = 0.1 - ((length - 10) / 200)`

- Very long snakes move at near-maximum speed

---

## Project Structure

```text
.
├── main.py        # Entry point and main game loop
├── snake.py       # Snake movement, growth, direction
├── food.py        # Normal & big food logic
├── scoreboard.py  # Score display and game-over handling
├── border.py      # Boundary drawing (Hard mode)
└── __pycache__/   # Python bytecode cache
```

---

## Suggestions for Improvement

- Save a **high score** to disk
- Add **pause / restart** controls
- Add sound effects (with extra libraries)
- Create a main menu screen
- Move configuration (speed, screen size, food odds) to a config file
- Improve testability by separating logic from rendering

---

## Troubleshooting

- If the Turtle window does not appear, ensure your system supports GUI windows.
- If the mode input dialog returns nothing, restart and enter **1** or **2**.

---

## License & Credits

**Author:** Adarsh Raj
