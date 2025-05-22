import sys

def run_maze_search():
    args_count = len(sys.argv)
    if args_count != 2:
        print("Please provide the input layout file in the command line")
        exit(0)

    input_file = sys.argv[1]

    maze_layout = []

    start = 'P'
    end = '.'
    space = ' '
    reverse = '#'
    move_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move_symbols = ['>', 'v', '<', '^']
    expanded_count = 0
    max_depth = 0
    max_fringe_size = 0

    def find_cell_location(cell):
        for index, locations in enumerate(maze_layout):
            try:
                return index, locations.index(cell)
            except ValueError:
                pass

    def get_cell_direction(location):
        row, col = location
        return maze_layout[row][col]

    def set_cell_direction(location, direction):
        row, col = location
        maze_layout[row][col] = direction

    def depth_first_search(maze_layout, location=None):
        nonlocal expanded_count, max_depth
        location = location or find_cell_location(start)

        if not location:
            return

        if get_cell_direction(location) == end:
            return location

        if get_cell_direction(location) not in (space, start):
            return

        for md in move_directions:
            next_cell = (location[0] + md[0], location[1] + md[1])
            mark_movement = move_symbols[move_directions.index(md)]

            if get_cell_direction(location) != start:
                set_cell_direction(location, mark_movement)

            solution = depth_first_search(maze_layout, next_cell)
            expanded_count += 1

            if solution:
                return solution

        max_depth += 1
        set_cell_direction(location, reverse)

    with open(input_file) as file:
        for line in file.read().splitlines():
            size = len(list(line))
            if size > max_fringe_size:
                max_fringe_size = size
            maze_layout.append(list(line))

    dfs_solution = depth_first_search(maze_layout)
    maze_layout_str = '\n'.join(''.join(r) for r in maze_layout)

    if dfs_solution:
        direction_marks = ['>', 'v', '<', '^', '#']
        for i in range(len(direction_marks)):
            maze_layout_str = maze_layout_str.replace(direction_marks[i], " ")
        print("SOLUTION")
        print(maze_layout_str)
        print('Path Cost:', dfs_solution)
        print("Number of Nodes Expanded:", expanded_count)
        print("Maximum Tree Depth Searched:", max_depth)
        print("Maximum size of the fringe:", max_fringe_size)
    else:
        print('No solution found')

if __name__ == "__main__":
    run_maze_search()
