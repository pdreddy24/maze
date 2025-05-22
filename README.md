# 🧩 Maze Solver using Depth-First Search (DFS)

This project implements a maze-solving algorithm in Python using the **Depth-First Search (DFS)** technique.

---

## 🔍 Overview

- The maze is represented as a 2D grid using Python lists.
- Based on graph theory, a *perfect maze* (no loops) resembles a tree.
- DFS is used to explore paths via backtracking, ideal for solving such mazes.

---

## 🗂 Maze Elements

| Symbol | Meaning       |
|--------|---------------|
| `P`    | Start Point   |
| `.`    | End Point     |
| `' '`  | Empty Space   |
| `#`    | Visited Path  |

---

## 🧭 Directions

Valid moves (row, column):

- Right → `(0, 1)` → `>`
- Down  → `(1, 0)` → `v`
- Left  → `(0, -1)` → `<`
- Up    → `(-1, 0)` → `^`

---

## 🧠 Key Functions

- `searchLocation(location)`: Finds the character at a given position.
- `getMazeDirection(location)`: Gets the direction of movement at a position.
- `setMazeDirection(location, direction)`: Marks a direction at a position in the maze.

---

