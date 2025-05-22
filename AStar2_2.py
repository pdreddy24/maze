import sys

# Check for the presence of the input layout file
args_count = len(sys.argv)
if args_count != 2:
    print("Please provide the input layout file in the command line")
    exit(0)

input_file = sys.argv[1]

# Initialize variables and constants
maze = []
start = 'P'        # Symbol for the starting point in the maze
end = '.'          # Symbol for the goal/end point in the maze
space = ' '        # Symbol for an empty space in the maze
reverse = '#'      # Symbol used for marking visited cells during search
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movement directions: right, down, left, up
directions = ['>', 'v', '<', '^']          # Symbols representing movement directions
expanded_count = 0   # Counter for the number of nodes expanded during search
max_depth = 0        # Counter for the maximum tree depth searched during search
max_fringe = 0       # Maximum size of the fringe during search

# Read the maze layout from the input file
with open(input_file) as file:
    for data in file.read().splitlines():
        size = len(data)
        if size > max_fringe:
            max_fringe = size
        maze.append(list(data))

# Function to calculate Manhattan distance between two points
def manhattan_distance(start, end):
    distance = 0
    for s, e in zip(start, end):
        distance += abs(s - e)
    return distance

# Find location of a particular cell symbol in the maze
def find_cell_location(cell):
    for index, locations in enumerate(maze):
        try:
            return index, locations.index(cell)
        except ValueError:
            pass

# Get the symbol representing the direction of movement at a specific location
def get_cell_direction(location):
    row, col = location
    return maze[row][col]

# Set the symbol representing the direction of movement at a specific location
def set_cell_direction(location, direction):
    row, col = location
    maze[row][col] = direction

# A* search algorithm to solve the maze
def a_star_search(maze_layout, location=None):
    global expanded_count, max_depth  # Declare as global
    
    location = location or find_cell_location(start)

    if not location:
        return

    if get_cell_direction(location) == end:
        return location

    if get_cell_direction(location) not in (space, start):
        return

    # Explore possible directions
    for md in dirs:
        next_cell = (location[0] + md[0], location[1] + md[1])
        manhattan_dist = manhattan_distance(location, next_cell)
        mark_movement = directions[dirs.index(md)]

        if get_cell_direction(location) != start:
            set_cell_direction(location, mark_movement)

        solution = a_star_search(maze_layout, next_cell)
        expanded_count += 1

        if solution:
            return solution

    max_depth += 1
    set_cell_direction(location, reverse)

# Execute A* search on the maze
dfs_solution = a_star_search(maze)
maze_layout_str = '\n'.join(''.join(r) for r in maze)

# Display the solution and related metrics
if dfs_solution:
    direction_symbols = ['>', 'v', '<', '^', '#', ' ']
    for i in range(len(direction_symbols)):
        maze_layout_str = maze_layout_str.replace(direction_symbols[i], " ")
    print("SOLUTION with A*")
    print(maze_layout_str)
    print('Path Cost:', dfs_solution)
    print("Number of Nodes Expanded:", expanded_count)
    print("Maximum Tree Depth Searched:", max_depth)
    print("Maximum size of the fringe:", max_fringe)
else:
    print('No solution found')
