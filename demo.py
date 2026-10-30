"""
Demo: Compare Minimax vs Alpha-Beta Pruning
"""

from alpha_beta import build_sample_tree, alpha_beta, minimax

if __name__ == '__main__':
    tree = build_sample_tree()

    print("=" * 50)
    print("ALPHA-BETA PRUNING DEMO")
    print("=" * 50)

    # Alpha-Beta
    ab_stats = {'visited': 0, 'pruned': 0}
    ab_result = alpha_beta(tree, depth=3, alpha=float('-inf'),
                           beta=float('inf'), maximizing=True, stats=ab_stats)

    # Minimax
    mm_stats = {'visited': 0}
    mm_result = minimax(tree, depth=3, maximizing=True, stats=mm_stats)

    print(f"\n📊 Results:")
    print(f"  Optimal value (Minimax)    : {mm_result}")
    print(f"  Optimal value (Alpha-Beta) : {ab_result}")

    print(f"\n🌳 Node statistics:")
    print(f"  Minimax visited     : {mm_stats['visited']} nodes")
    print(f"  Alpha-Beta visited  : {ab_stats['visited']} nodes")
    print(f"  Alpha-Beta pruned   : {ab_stats['pruned']} branches")
    print(f"\n  Efficiency gain: "
          f"{100 * (1 - ab_stats['visited'] / mm_stats['visited']):.1f}%")
    print("=" * 50)