from planners import bfs, ucs, astar, local_search
from utils import load_map
import sys

if __name__ == "__main__":
    # check if enough command line args are given
    if len(sys.argv) < 3:
        print("Usage: python agents.py <map_file> <algorithm>")
        sys.exit(1)

    # taking inputs
    map_file = sys.argv[1]
    algo = sys.argv[2]

    # load map from file (grid, start and goal positions)
    grid, start, goal = load_map(map_file)

    print("📦 Delivery Agent Started!")
    print(f"Map: {map_file}")
    print(f"Start: {start}, Goal: {goal}")
    print(f"Algorithm: {algo}\n")

    # run the selected algorithm
    if algo == "bfs":
        path, cost = bfs(grid, start, goal)
    elif algo == "ucs":
        path, cost = ucs(grid, start, goal)
    elif algo == "astar":
        path, cost = astar(grid, start, goal)
    elif algo == "local":
        path, cost = local_search(grid, start, goal)
    else:
        print("❌ Unknown algorithm! Choose from bfs / ucs / astar / local")
        sys.exit(1)
    
    def print_path_on_grid(grid, path):
        """
        Prints the grid showing the path.
        S = Start, G = Goal, * = Path, # = obstacle, . = empty
        """
        visual_grid = [row[:] for row in grid]  # make a copy so we don't modify the original

        start = path[0]
        goal = path[-1]

        for r, c in path[1:-1]:  # mark path except start & goal
            visual_grid[r][c] = '*'

        visual_grid[start[0]][start[1]] = 'S'
        visual_grid[goal[0]][goal[1]] = 'G'

        for row in visual_grid:
            print(' '.join(str(cell) if cell in ['#', '*', 'S', 'G'] else '.' for cell in row))
        print()  # blank line at the end

    # print the results
    if path:
        print("✅ Path found!")
        print("Path:", path)
        print("Total Cost:", cost)
        print("Path length:", len(path))
        print_path_on_grid(grid, path)

    else:
        print("❌ No path found! Maybe obstacles are blocking the way.")
    
   