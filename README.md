# Alpha-Beta Pruning 🎯

A Python implementation of the **Alpha-Beta Pruning** algorithm — an optimization of the Minimax algorithm used in game theory and artificial intelligence.

## 📖 What is Alpha-Beta Pruning?

Alpha-Beta Pruning is a search algorithm that reduces the number of nodes evaluated by the Minimax algorithm in its search tree. It's widely used in two-player games like Chess, Checkers, and Tic-Tac-Toe.

- **Alpha (α)**: The best value the maximizer can guarantee so far
- **Beta (β)**: The best value the minimizer can guarantee so far
- When **α ≥ β**, we can prune the remaining branches

## ⚡ Complexity

| Algorithm | Time Complexity |
|-----------|-----------------|
| Minimax | O(b^d) |
| Alpha-Beta (best case) | O(b^(d/2)) |
| Alpha-Beta (average) | ~O(b^(3d/4)) |

Where `b` = branching factor, `d` = depth.

## 🚀 Usage

```bash
python demo.py
