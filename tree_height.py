import sys
import threading
import numpy


def compute_height(n, parents):
    # Create an array to store the height of each node in the tree
    heights = numpy.zeros(n, dtype=int)

    # Iterate over each node in the tree
    for node in range(n):
        # If the node is the root, set its height to 1
        if parents[node] == -1:
            heights[node] = 1
        else:
            # If the node is not the root, calculate its height as the height of its parent plus 1
            # and update the maximum height if necessary
            heights[node] = heights[parents[node]] + 1
            max_height = max(max_height, heights[node])

    # Return the maximum height of the tree
    return max_height


def main():
    # Accept user input from stdin or from a file
    input_type = input("Enter 'f' to read input from a file or 'i' to read input from keyboard: ").lower()
    if input_type == 'f':
        # Input filename
        file_path = input("Enter the file path (without the extension): ")
        if not os.path.isfile(f"{file_path}.txt"):
            print("File not found.")
            return

        try:
            # Read input from file
            with open(f"{file_path}.txt") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except ValueError:
            print("Invalid input.")
            return
    elif input_type == 'i':
        # Input number of nodes
        try:
            n = int(input("Enter the number of nodes: "))
        except ValueError:
            print("Invalid input.")
            return

        # Input parent values
        parents = []
        for i in range(n):
            try:
                parent = int(input(f"Enter the parent of node {i}: "))
            except ValueError:
                print("Invalid input.")
                return
            parents.append(parent)
    else:
        print("Invalid input.")
        return

    # Calculate the height of the tree
    tree_height = compute_height(n, parents)

    # Output the result
    print("Height of the tree:", tree_height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
