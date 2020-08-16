N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

result = list(map(lambda x: str(int(x in A)), nums))

print('\n'.join(result))