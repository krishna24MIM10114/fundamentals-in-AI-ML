# Delivery Agent Pathfinding

## Description
This project implements a delivery agent that finds the shortest path from a start location to a goal on a 2D grid map using multiple search algorithms: *Breadth-First Search (BFS), **Uniform Cost Search (UCS), **A Search*, and **Local Search*. The agent avoids obstacles, calculates path cost, and displays the path visually on the grid.

## Features
- BFS, UCS, A*, and Local Search pathfinding
- Visual grid representation of the path
- Outputs total cost and path length
- Supports multiple map files (Dynamic, Small, Medium, Large)

## Installation / Setup
```bash
git clone <your-repo-url>
cd AIML_Project/src

How to Run

python agents.py ../Maps/small.txt bfs         # Run BFS on Small map
python agents_dynamic.py ../Maps/dynamic.txt astar  # Run A* on Dynamic map
python agents.py ../Maps/medium.txt ucs       # Run UCS on Medium map
python agents.py ../Maps/large.txt local      # Run Local Search on Large map

Output Example (BFS)

📦 Delivery Agent Started!
Map: ../maps/small.txt
Start: (0, 0), Goal: (4, 8)
Algorithm: bfs

✅ Path found!
Path: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
Total Cost: 13
Path length: 13
S . . . . . . . .
* . . . . . . . .
* . . . . . . . .
* . . . . . . . .
* * * * * * * * G

Directory Structure

AIML_Project/
├── Maps/
│   ├── dynamic.txt
│   ├── large.txt
│   ├── medium.txt
│   └── small.txt
├── Report/
├── Result/
│   └── logs.txt
├── Src/
│   ├── agent_dynamic.py
│   ├── agents.py
│   ├── planners.py
│   └── utils.py
└── README.md

Future Work

Animate the agent moving step-by-step
Add weighted maps for UCS and A*
Colored visual output for better clarity
Improve Local Search heuristics

Author

Soumya Pandey