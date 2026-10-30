from alpha_beta import alpha_beta

result = alpha_beta(
    node,
    depth=5,
    alpha=float('-inf'),
    beta=float('inf'),
    maximizing=True
)
