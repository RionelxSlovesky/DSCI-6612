
# 📘 Course Information

**Course:** DSCI 6612  
**Instructor:** Dr. Shivanjali Khare  

**Team Members:**
1. Ahmed Omar Salim Adnan – [aadna1@unh.newhaven.edu](mailto:aadna1@unh.newhaven.edu)  
2. Gowtham Chebrolu – [gcheb1@unh.newhaven.edu](mailto:gcheb1@unh.newhaven.edu)  
3. Ishika Dubey – [idube1@unh.newhaven.edu](mailto:idube1@unh.newhaven.edu)  

---

# 🔄 8-Puzzle Solver (Mid-Project Status)

This project implements and compares classical search algorithms to solve the **8-puzzle problem** — a 3x3 sliding tile puzzle where the goal is to reach a target configuration from a shuffled state by moving tiles.

---

## ✅ Objective

To evaluate and compare the **efficiency**, **optimality**, and **scalability** of the following algorithms:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform Cost Search (UCS)**
- **A\* Search** (using Manhattan or Hamming heuristics)

---

## 🧠 Algorithms Implemented

- **BFS** – Explores all nodes at the current depth before going deeper. Guarantees optimal path but uses high memory.
- **DFS** – Explores as deep as possible along a branch. Uses less memory but may be suboptimal and get stuck in cycles.
- **UCS** – Expands the least-cost node using a priority queue. Similar to Dijkstra’s algorithm.
- **A\*** – Informed search using `f(n) = g(n) + h(n)`:
  - `g(n)` = cost to reach current node
  - `h(n)` = heuristic estimate to goal (e.g., Manhattan distance)

---

## 🧪 Features

- CLI to choose:
  - Start state
  - Search algorithm
  - Heuristic (if A\* selected)
- Animated **Matplotlib visualization** of solution path
- Modular architecture with separate folders for:
  - `algorithms/`
  - `heuristics/`
  - `visualization/`

---

## 🚀 How to Run

1. Install requirements:
   ```bash
   pip install matplotlib
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the prompts to select algorithm and puzzle configuration.

---

## 🎥 Presentation Video

📺 [Watch our project walkthrough](https://youtu.be/VRfdUV0MV5Q)

---

## 📚 References

- [IEEE: Analysis of Tree-Based Search Techniques for Solving 8-Puzzle Problem](https://ieeexplore.ieee.org/document/8257061)  
- [Springer: Comparative Analysis of AI-Based Search Algorithms](https://doi.org/10.1186/s42269-024-01274-3)
