from search_algorithms import astar
from heuristics import manhattan_distance

if __name__ == "__main__":
    start = [[2, 8, 3],
             [1, 6, 4],
             [7, 0, 5]]
    goal = [[1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]]

    path = astar(start, goal, heuristic=manhattan_distance)

    if path:
        print("Solution path:")
        for state in path:
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")
