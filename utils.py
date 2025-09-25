def load_grid(filename):
    """
    Load a grid from a text file.
    - 'S' = start
    - 'G' = goal
    - 'X' = obstacle (impassable)
    - numbers = terrain cost
    Returns: grid (2D list), start, goal
    """
    grid = []
    start = None
    goal = None

    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            row = []
            for j, val in enumerate(line.strip().split()):
                if val == 'S':
                    start = (i,j)
                    row.append(1)  # assume start cost = 1
                elif val == 'G':
                    goal = (i,j)
                    row.append(1)  # assume goal cost = 1
                elif val == 'X':
                    row.append(float('inf'))  # impassable
                else:
                    row.append(int(val))
            grid.append(row)
    return grid, start, goal


def print_grid(grid, path=None):
    """
    Print the grid nicely.
    If path is given, mark it with '*'
    """
    path_set = set(path) if path else set()
    for i,row in enumerate(grid):
        line = ''
        for j,val in enumerate(row):
            if (i,j) in path_set:
                line += ' * '
            elif val == float('inf'):
                line += ' X '
            else:
                line += f'{val:2d} '
        print(line)
    print()

def load_map(file_path):
    grid = []
    start = None
    goal = None

    with open(file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        row = []
        for j, ch in enumerate(line.strip()):
            if ch == "S":
                start = (i, j)
                row.append(1)
            elif ch == "G":
                goal = (i, j)
                row.append(1)
            elif ch == "X":  # obstacle
                row.append(-1)
            else:  # normal terrain
                row.append(1)
        grid.append(row)

    if start is None or goal is None:
        raise ValueError("Map file must contain 'S' (start) and 'G' (goal)!")

    return grid, start, goal