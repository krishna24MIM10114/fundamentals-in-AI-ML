import time
from utils import load_grid, print_grid
from planners import local_search

def run_dynamic_agent(mapfile):
    grid, start, goal = load_grid(mapfile)
    print("Start:", start, "Goal:", goal)

    # Define moving obstacles (simulate them moving over time)
    moving_obs = [(1,2), (2,2), (3,2)]  # this obstacle moves down each step
    obstacle_index = 0  # where the obstacle is currently

    cur_pos = start
    path, cost, nodes = local_search.local_search(grid, cur_pos, goal, [])

    while cur_pos != goal:
        # Place the current dynamic obstacle on grid
        if obstacle_index < len(moving_obs):
            obs = moving_obs[obstacle_index]
            grid[obs[0]][obs[1]] = float('inf')  # block cell

        # Check if next step in path is blocked
        next_step = path[1] if len(path) > 1 else path[0]
        if grid[next_step[0]][next_step[1]] == float('inf'):
            print(f"Obstacle at {next_step}! Replanning...")
            path, cost, nodes = local_search.local_search(grid, cur_pos, goal, [])
        
        # Move agent one step
        cur_pos = path[1] if len(path) > 1 else path[0]
        path = path[1:]  # update path
        print_grid(grid, path=[cur_pos])
        time.sleep(0.5)  # just for demo to see movement

        # Move the obstacle to next position
        if obstacle_index < len(moving_obs)-1:
            # clear previous obstacle
            grid[moving_obs[obstacle_index][0]][moving_obs[obstacle_index][1]] = 1
            obstacle_index += 1

    print("Reached goal!")