import sys

def main():
    # Check if the correct number of arguments are provided
    arguments_count = len(sys.argv)
    if arguments_count != 2:
        print("Please specify the maze layout file when running the program")
        exit(0)
    
    # Retrieve the input file name from command line arguments
    input_file = sys.argv[1]

    # Initialize variables for maze layout and traversal
    maze_layout = []
    start_node = 'P'
    end_node = '.'
    empty_node = ' '
    reverse_node = '#'
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_symbols = ['>', 'v', '<', '^']  # Symbols to represent movement
    expanded_node_count = 0  # Counter to track the number of nodes expanded
    search_tree_depth = 0  # Variable to track maximum depth of the search tree
    fringe_max_size = 0  # Variable to track maximum size of the fringe (frontier)

    # Read the maze layout from the input file
    with open(input_file) as maze_file:
        for maze_row_data in maze_file.read().splitlines():
            row_size = len(list(maze_row_data))
            if row_size > fringe_max_size:
                fringe_max_size = row_size
            maze_layout.append(list(maze_row_data))

     # Function to get the character at a specific location in the maze
    def get_maze_direction(location):
        row, col = location
        return maze_layout[row][col]

    # Function to set a specific character at a given location in the maze
    def set_maze_direction(location, direction):
        row, col = location
        maze_layout[row][col] = direction

    # Function to find the location of a given character in the maze
    def locate_char_position(char):
        for row_index, row_locations in enumerate(maze_layout):
            try:
                return row_index, row_locations.index(char)
            except:
                pass


    # Depth First Search (DFS) algorithm for maze traversal
    def depth_first_search(maze, location=None, direction=None):
        nonlocal expanded_node_count, search_tree_depth
        location = location or locate_char_position(start_node)  # Start from the given location or find the start location

        # If no location is found, return
        if not location:
            return

        # If the current location is the end point, return it
        if get_maze_direction(location) == end_node:
            return location

        # If the current location is not empty or the start point, return
        if get_maze_direction(location) not in (empty_node, start_node):
            return

        # Explore all possible directions
        for md in directions:
            next_cell = (location[0] + md[0], location[1] + md[1])  # Calculate next cell coordinates
            mark_movement = direction_symbols[directions.index(md)]  # Get the symbol for the movement direction

            # Mark the movement direction in the maze
            if get_maze_direction(location) != start_node:
                set_maze_direction(location, mark_movement)

            # Recursively call DFS for the next cell
            solution = depth_first_search(maze, next_cell, md)
            expanded_node_count += 1   # Increment the node expansion count

            # If solution is found, return it
            if solution:
                return solution

        search_tree_depth += 1  # Update maximum tree depth
        set_maze_direction(location, reverse_node)  # Mark the reverse movement direction

    # Perform DFS traversal of the maze
    dfs_solution = depth_first_search(maze_layout)
    
    # Convert maze layout to string format for printing
    maze_layout = '\n'.join(''.join(r) for r in maze_layout)
    
    # Print the solution and traversal statistics
    if dfs_solution:
        direction_marks = ['>', 'v', '<', '^', '#']
        for i in range(len(direction_marks)):
            maze_layout = maze_layout.replace(direction_marks[i], ".")
        print("SOLUTION")
        print(maze_layout)
        print('Path Cost:', dfs_solution)
        print("Number of Nodes Expanded:", expanded_node_count)
        print("Maximum Tree Depth Searched:", search_tree_depth)
        print("Maximum size of the fringe:", fringe_max_size)
    else:
        print('No solution found')

if __name__ == "__main__":
    main()
