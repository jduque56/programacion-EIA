def dfs(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current == end:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(maze, current):
            stack.append(neighbor)

    return False

def get_neighbors(maze, current):
    neighbors = []

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = current[0] + dx, current[1] + dy

        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == '#':
            continue

        neighbors.append((x, y))

    return neighbors

maze = [
    ['#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#'],
]

start = (1, 1)
end = (3, 3)

print(dfs(maze, start, end))
