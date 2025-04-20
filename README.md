# 📘 Course Information

**Course:** DSCI 6612  
**Instructor:** Dr. Shivanjali Khare  

**Team Members:**
1. Ahmed Omar Salim Adnan – [aadna1@unh.newhaven.edu](mailto:aadna1@unh.newhaven.edu)  
2. Gowtham Chebrolu – [gcheb1@unh.newhaven.edu](mailto:gcheb1@unh.newhaven.edu)  
3. Ishika Dubey – [idube1@unh.newhaven.edu](mailto:idube1@unh.newhaven.edu)  

# 8-Puzzle Solver (Mid-Project Status)

This project implements and compares classical search algorithms to solve the **8-puzzle problem** — a 3x3 sliding tile puzzle that challenges an agent to reach a goal state from a shuffled configuration.

## ✅ Objective

To evaluate and compare the **efficiency**, **optimality**, and **scalability** of:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform Cost Search (UCS)**
- **A\* Search (with Manhattan Distance heuristic)**

## 🧠 Algorithms Implemented

- **BFS** – Guarantees optimal path but consumes high memory.
- **DFS** – Explores deep paths quickly but may miss optimal solutions and get stuck in loops.
- **UCS** – Baseline uninformed search using cost-based priority.
- **A\*** – Informed search with `f(n) = g(n) + h(n)` using Manhattan heuristic.

## 📌 Usage

Run the main script:

```bash
python main.py
```

## 📚 References

- [Analysis of Tree-Based Search Techniques for Solving 8-Puzzle Problem (IEEE)](https://ieeexplore.ieee.org/document/8257061)  
- [Comparative Analysis of AI-Based Search Algorithms (Springer Open)](https://doi.org/10.1186/s42269-024-01274-3)

---


