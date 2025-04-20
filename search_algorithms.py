from puzzle import Puzzle
from queue import Queue, PriorityQueue
from itertools import count

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

def bfs(start, goal):
    start_node = Puzzle(start)
    frontier = Queue()
    frontier.put(start_node)
    explored = set()

    while not frontier.empty():
        node = frontier.get()
        if node.state == goal:
            return reconstruct_path(node)
        explored.add(str(node.state))
        for neighbor in node.get_neighbors():
            if str(neighbor.state) not in explored:
                frontier.put(neighbor)
    return None

def dfs(start, goal):
    start_node = Puzzle(start)
    stack = [start_node]
    explored = set()

    while stack:
        node = stack.pop()
        if node.state == goal:
            return reconstruct_path(node)
        explored.add(str(node.state))
        for neighbor in reversed(node.get_neighbors()):
            if str(neighbor.state) not in explored:
                stack.append(neighbor)
    return None

def ucs(start, goal):
    start_node = Puzzle(start)
    frontier = PriorityQueue()
    tie_breaker = count()
    frontier.put((0, next(tie_breaker), start_node))
    explored = set()

    while not frontier.empty():
        _, _, node = frontier.get()
        if node.state == goal:
            return reconstruct_path(node)
        explored.add(str(node.state))
        for neighbor in node.get_neighbors():
            if str(neighbor.state) not in explored:
                frontier.put((neighbor.cost, next(tie_breaker), neighbor))
    return None

def astar(start, goal, heuristic):
    start_node = Puzzle(start)
    frontier = PriorityQueue()
    tie_breaker = count()
    frontier.put((heuristic(start_node.state, goal), next(tie_breaker), start_node))
    explored = set()

    while not frontier.empty():
        _, _, node = frontier.get()
        if node.state == goal:
            return reconstruct_path(node)
        explored.add(str(node.state))
        for neighbor in node.get_neighbors():
            if str(neighbor.state) not in explored:
                h = heuristic(neighbor.state, goal)
                frontier.put((neighbor.cost + h, next(tie_breaker), neighbor))
    return None
