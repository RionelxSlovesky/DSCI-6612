import matplotlib.pyplot as plt
import matplotlib.animation as animation

class PuzzleVisualizer:
    def __init__(self, state_sequence):
        self.state_sequence = state_sequence
        self.fig, self.ax = plt.subplots()

        self.fig.subplots_adjust(
            left=0.125,
            bottom=0.11,
            right=0.385,
            top=0.39,
            wspace=0.2,
            hspace=0.2
        )

        self.text_grid = [[None for _ in range(3)] for _ in range(3)]

    def draw_state(self, state):
        self.ax.clear()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        for i in range(3):
            for j in range(3):
                val = state[i][j]
                color = 'lightgray' if val == 0 else 'skyblue'
                self.ax.add_patch(plt.Rectangle((j, 2 - i), 1, 1, edgecolor='black', facecolor=color))
                if val != 0:
                    self.ax.text(j + 0.5, 2.5 - i, str(val), ha='center', va='center', fontsize=16)

    def animate(self, i):
        state = self.state_sequence[i]
        self.draw_state(state)

    def show(self):
        
        self.ani = animation.FuncAnimation(
            self.fig,
            self.animate,
            frames=len(self.state_sequence),
            interval=1000,
            repeat=False
        )
        plt.show()
