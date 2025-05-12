from algorithms.search_algorithms import astar, bfs, dfs, ucs
from heuristics.heuristics import manhattan_distance, hamming_distance
from visualization.visualizer import PuzzleVisualizer

def select_start_state():
    start_states = [
        [[0, 2, 1],
         [6, 3, 4],
         [7, 5, 8]],
        
        [[2, 8, 3],
         [1, 6, 4],
         [7, 0, 5]]

    ]

    print("Choose a start state:")
    for i, state in enumerate(start_states):
        print(f"\n{i+1}.")
        for row in state:
            print(row)

    choice = int(input("\nEnter the number of the start state: ")) - 1
    if 0 <= choice < len(start_states):
        return start_states[choice]
    else:
        print("Invalid choice. Defaulting to option 1.")
        return start_states[0]

def select_algorithm():
    print("\nChoose a search algorithm:")
    print("1. A* Search")
    print("2. Breadth-First Search (BFS)")
    print("3. Depth-First Search (DFS)")
    print("4. Uniform Cost Search (UCS)")
    return input("Enter the number of the algorithm: ").strip()

def select_heuristic():
    print("\nChoose a heuristic for A*:")
    print("1. Manhattan Distance")
    print("2. Hamming Distance")
    return input("Enter the number of the heuristic: ").strip()

if __name__ == "__main__":
    start = select_start_state()
    goal = [[1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]]

    algo_choice = select_algorithm()

    if algo_choice == '1':
        heuristic_choice = select_heuristic()
        heuristic = manhattan_distance if heuristic_choice == '1' else hamming_distance
        path = astar(start, goal, heuristic=heuristic)
    elif algo_choice == '2':
        path = bfs(start, goal)
    elif algo_choice == '3':
        path = dfs(start, goal)
    elif algo_choice == '4':
        path = ucs(start, goal)
    else:
        print("Invalid choice.")
        exit()

    if path:
        print("\n✅ Solution path:")
        for state in path:
            for row in state:
                print(row)
            print()
        visualizer = PuzzleVisualizer(path)
        visualizer.show()
    else:
        print("\n❌ No solution found.")
