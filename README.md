# Number Guessing Game

The idea for [this project](https://roadmap.sh/projects/number-guessing-game) was taken from [roadmap.sh backend projects](https://roadmap.sh/backend/projects)

## Overview

This is a simple **Number Guessing Game** implemented in Python. Players attempt to guess a randomly generated number within a specified range, choosing from three difficulty levels. The game tracks statistics for each difficulty level and saves them persistently to a JSON file.

---

## Features

- **Multiple Difficulty Levels**:
  - **Easy**: 10 attempts
  - **Medium**: 5 attempts
  - **Hard**: 3 attempts
- **Hints**: Provides hints if the player struggles.
- **Statistics Tracking**: Keeps track of wins by difficulty level.
- **Persistent Storage**: Saves victory stats to `data.json`.

---

## How to Play

1. Run the game script using:
   ```bash
   python main.py
