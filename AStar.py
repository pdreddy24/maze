import sys

def main():
    # Check if the correct number of arguments are provided in the command line
    if len(sys.argv) != 2:
        print("Please provide input maze file")
        exit(0)
    
    # Get the input file name from the command line argument
    input_file = sys.argv[1]

    # Initialize variables and lists for maze layout and search parameters
    layout = []
    start_node = 'P'
    end_node = '.'
    empty_node = ' '
    reverse_node = '#'
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_nodes = ['>', 'v', '<', '^']  # Symbols to represent movement
    expanded_node_count = 0  # Counter to track the number of nodes expanded
    search_tree_depth = 0  # Variable to track maximum depth of the search tree
    fringe_max_size = 0  # Variable to track maximum size of the fringe

    # Read the maze layout from the input file
    with open(input_file) as maze_file:
        for maze_row_data in maze_file.read().splitlines():
            row_size = len(maze_row_data)
            if row_size > fringe_max_size:
                fringe_max_size = row_size
            layout.append(list(maze_row_data))

    # Function to calculate Manhattan distance between two points
    def manhattan_distance(start, end):
        distance_value = 0
        for start_pos, end_pos in zip(start, end):
            distance_value += abs(start_pos - end_pos)
        return distance_value

    # Function to find the location of a character in the maze layout
    def locate_char_position(location):
        for index, locations in enumerate(layout):
            try:
                return index, locations.index(location)
            except:
                pass

    # Function to get the character at a given location in the maze layout
    def get_maze_direction(location):
        row, col = location
        return layout[row][col]

    # Function to set a specific character at a given location in the maze
    def set_maze_direction(location, direction):
        row, col = location
        layout[row][col] = direction

    # Recursive A* search algorithm to find the path from start to end
    def a_star(maze_layout, location=None):
        nonlocal expanded_node_count, search_tree_depth
        location = location or locate_char_position(start_node)

        if not location:
            return

        if get_maze_direction(location) == end_node:
            return location

        if get_maze_direction(location) not in (empty_node, start_node):
            return

        for md in directions:
            next_location = (location[0] + md[0], location[1] + md[1])
            mark_movement = direction_nodes[directions.index(md)]

            if get_maze_direction(location) != start_node:
                set_maze_direction(location, mark_movement)

            solution = a_star(maze_layout, next_location)
            expanded_node_count += 1

            if solution:
                return solution

        search_tree_depth += 1
        set_maze_direction(location, reverse_node)

    # Perform A* search to find the solution
    dfs_solution = a_star(layout)

    # Format maze layout as a string for display
    layout = '\n'.join(''.join(r) for r in layout)

    # Print the solution and search statistics
    if dfs_solution:
        direction_marks = ['>', 'v', '<', '^', '#']
        for i in range(len(direction_nodes)):
            layout = layout.replace(direction_nodes[i], ".")
        print("SOLUTION with A*")
        print(layout)
        print('Path Cost:', dfs_solution)
        print("Number of Nodes Expanded:", expanded_node_count)
        print("Maximum Tree Depth Searched:", search_tree_depth)
        print("Maximum size of the fringe:", fringe_max_size)
    else:
        print('No solution found')

if __name__ == "__main__":
    main()
