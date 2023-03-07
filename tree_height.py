# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Izveido masīvu, kurā glabāt visus kokus
    trees = [0] * n

    # Katram masīva elementam aprēķina augstumu
    for node in range(n):
        # Ja elementam augstums ir jau aprēķināts, tas tiek izlaists
        if trees[node] != 0:
            continue

        # Ja elements nav vēl aprēķināts, to aprēķina, izmantojot tā 'paternts'
        height = 0
        while node != -1:
            if trees[node] != 0:
                height += trees[node]
                break
            height += 1
            node = parents[node]
        trees[node] = height

    # Koka garums ir lielākā iespējamā vērtība jebkuram elementam
    return max(trees)

def main():
    # Pavaicā lietotājam, vai vēlās ievadīt no klavietūras, vai no faila
    I_or_F = input("Enter 'I' for manual input or 'F' for file input: ").strip().upper()

    if I_or_F == 'I':
        # Klavietūras ievade
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent indices, separated by spaces: ").split()))
    elif I_or_F == 'F':
        # Faila ievade
        file_name = input("Enter the name of the input file (in 'folder/filename' format): ")
        if 'a' in file_name:
            print("Invalid filename: cannot contain the letter 'a'")
            return

        try:
            with open(file_name, 'r') as chosen_file:
                n = int(chosen_file.readline().strip())
                parents = list(map(int, chosen_file.readline().strip().split()))
        except FileNotFoundError:
            print("File not found")
            return
    else:
        # Kļūme - nederīga ievade
        print("Invalid input source")
        return

    # Koka garuma aprēķins
    height = compute_height(n, parents)
    print("The height of the tree is:", height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

main()
print(numpy.array([1,2,3]))
