from numpy import array as array
from copy import deepcopy
from itertools import permutations


N, M, K = map(int, input().split())
origin_A = [list(map(int, input().split())) for i in range(N)]
rotate = [list(map(int, input().split())) for i in range(K)]


origin_A = array(origin_A)
ans = 10*5
for try_rotation in list(permutations(rotate, K)):
    A = deepcopy(origin_A)
    for r,c,s in try_rotation:
        rotate_A(r, c, s)
    ans = min(ans, min(list(map(sum, A))))

print(ans)

def rotate_A(r, c, s):
    if s <= 0:
        return
    else:
        l_row, l_col, r_row, r_col = r-s-1, c-s-1, r+s-1, c+s-1

        # 테두리 값 바꿔주기
        up = deepcopy(A[l_row,l_col: r_col+1])
        down = deepcopy(A[r_row,l_col: r_col+1])
        left = deepcopy(A[l_row:r_row+1,l_col]) 
        right = deepcopy(A[l_row:r_row+1,r_col])
        

        up, down, left, right = np.append(left[1],up)[:-1], np.append(down,right[-2])[1:], left[2:2+s+1], right[:s+1]
        A[l_row,l_col:r_col+1] = up
        A[r_row,l_col: r_col+1] = down
        if s == 1:
            A[l_row+1,l_col] = left[0]
            A[l_row+1,r_col] = right[0]
        else:
            A[l_row+1:r_row,l_col] = left
            A[l_row+1:r_row,r_col] = right
        rotate_A(r, c, s-1)