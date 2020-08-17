N = int(input())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)
[print(i) for i in num_list]