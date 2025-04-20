import copy

class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_neighbors(self):
        neighbors = []
        i, j = self.get_blank_position()
        directions = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
        for move, (di, dj) in directions.items():
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = copy.deepcopy(self.state)
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(Puzzle(new_state, self, move, self.depth + 1, self.cost + 1))
        return neighbors

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))
