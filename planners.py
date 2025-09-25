#**************************A Star******************
import heapq

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    heap = [(manhattan(start,goal), 0, start)]  # (f_score, g_cost, cell)
    came_from = {}
    cost_so_far = {start: 0}
    checked = set()
    nodes_checked = 0

    while heap:
        f, g, cur = heapq.heappop(heap)
        nodes_checked += 1

        if cur == goal:
            break
        if cur in checked:
            continue
        checked.add(cur)

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cur[0]+dx, cur[1]+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] != float('inf'):
                    new_g = g + grid[nx][ny]
                    if (nx,ny) not in cost_so_far or new_g < cost_so_far[(nx,ny)]:
                        cost_so_far[(nx,ny)] = new_g
                        new_f = new_g + manhattan((nx,ny), goal)
                        heapq.heappush(heap, (new_f, new_g, (nx,ny)))
                        came_from[(nx,ny)] = cur

    # reconstruct path
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from.get(cur, start)
    path.append(start)
    path.reverse()

    total_cost = sum([grid[x][y] for x,y in path])
    return path, total_cost, nodes_checked

# ******************************bfs *************

from collections import deque

def bfs(grid, start, goal):
    """
    Breadth First Search (BFS)
    It explores all nodes level by level and finds the shortest path (in steps).
    """

    # queue to explore nodes
    q = deque([start])
    # set to keep track of visited nodes
    visited = set([start])
    # dictionary to reconstruct the path later
    parent = {start: None}

    # BFS loop
    while q:
        current = q.popleft()

        # if we reached the goal, stop searching
        if current == goal:
            break

        x, y = current
        # all 4 possible moves (up, down, left, right)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            # check if the next cell is valid and not a wall (-1 means obstacle)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != -1:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current
                    q.append((nx, ny))

    # if goal not found, return None
    if goal not in parent:
        return None, 0

    # reconstruct the path from goal to start
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    # cost = number of steps
    return path, len(path) 


# ****************** local search*****************

def local_search(grid, start, goal, dynamic_obstacles):
    """
    This is a simple version of dynamic replanning:
    - If a dynamic obstacle is on the path, we just recalc UCS.
    - Later you can make it smarter (hill-climb, random restart)
    """
    # For now just run UCS
    path, cost, nodes = ucs(grid, start, goal)

    # pretend we're checking dynamic obstacles
    for obs in dynamic_obstacles:
        if obs in path:
            print("Obstacle in path! Replanning...")
            path, cost, nodes = ucs(grid, start, goal)  # recalc path
            break

    return path, cost, nodes

# ***************************ucs**************

import heapq

def ucs(grid, start, goal):
    heap = [(0, start)]  # (cost so far, current cell)
    came_from = {}
    cost_so_far = {start: 0}
    checked = set()
    nodes_checked = 0

    while heap:
        cur_cost, cur_cell = heapq.heappop(heap)
        nodes_checked += 1

        if cur_cell == goal:
            break
        if cur_cell in checked:
            continue
        checked.add(cur_cell)

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cur_cell[0]+dx, cur_cell[1]+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] != float('inf'):
                    new_cost = cur_cost + grid[nx][ny]
                    if (nx,ny) not in cost_so_far or new_cost < cost_so_far[(nx,ny)]:
                        cost_so_far[(nx,ny)] = new_cost
                        heapq.heappush(heap, (new_cost, (nx,ny)))
                        came_from[(nx,ny)] = cur_cell

    # Reconstruct path
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from.get(cur, start)
    path.append(start)
    path.reverse()

    total_cost = sum([grid[x][y] for x,y in path])
    return path, total_cost, nodes_checked