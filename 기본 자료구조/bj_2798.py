from itertools import combinations
N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))

comb = list(combinations(cards, 3))
total = list(map(sum, comb))
comb = list(map(lambda x: M-x, total))
comb = [total[x] for x, y in enumerate(comb) if y >= 0]
ans = sorted(comb)[-1]
print(ans)