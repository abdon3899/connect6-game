# connect6 game

Connect6 is a strategic two-player game inspired by classics like Connect 4 and Go Moku. Played on a grid (commonly a 19x19 board), players alternate turns placing two stones per move, except for the first player, who starts with one stone only. The goal is to form a line of six consecutive stones horizontally, vertically, or diagonally.

# Connect6 Game Architecture

This document outlines the key components and their functionalities within the Connect6 game application.

---

## UI (User Interface)

This section manages the **graphical user interface** for the game. It comprises two primary classes:

- **UI**: Handles the main **menu** and the **general game setup**.
- **Connect6**: Represents the **game board** and manages the **gameplay**, including logic for various **game modes**.

---

## Board

The **Board** class is responsible for **creating the game board**. Its instance is used by other classes to manage the board's **state** and facilitate **gameplay**.

---

## Logic

This component contains the **core game logic**, including functions for **switching players**, **placing pieces** on the board, and other **essential operations**. It is the central part of the application, ensuring **smooth gameplay**.

---

## Minimax

The **Minimax** class implements the **Minimax algorithm** to determine the **best move for the AI**. The algorithm evaluates the game board and identifies the **optimal position** for the AI, considering a **search depth of 3**. The evaluation of the board is performed by the `evaluate board` method, which guides the AI's decisions.

---

## Alphabet (Alpha-Beta Pruning)

**Alpha-Beta Pruning** is an **optimization** of the Minimax algorithm. It significantly **reduces time complexity** by pruning branches of the search tree that do not need to be explored. This method is much **faster than Minimax** while providing nearly the same output, making it more efficient.

---

## Heuristic 1 and Heuristic 2

These are **improved versions** of the `evaluate board` method used in both the Minimax and Alpha-Beta algorithms.

- **Heuristic 1**: Focuses on **controlling the center of the board** and **increasing the number of open ends**, thereby improving the chances of winning.
- **Heuristic 2**: Concentrates more on the **opponent's move patterns**, aiming to **block or counter their strategic placements**.
