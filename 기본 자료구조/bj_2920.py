sing = list(map(int, input().split()))
flag = True

if (sing[0] > sing[1]) & (sing[0] == 8):
    ans = 'desecending'
elif (sing[0] < sing[1]) & (sing[0] == 1):
    ans = 'ascending'

else:
    flag = False
    ans = 'mixed'

i = 1

while (flag == True) & (i<=len(sing)-2):

    if ans == 'descending':
        if sing[i]-1 == sing[i+1]:
            i=i+1
            continue
        else:
            flag = False
            ans = 'mixed'
    else:
        if sing[i]+1 == sing[i+1]:
            i=i+1
            continue
        
        else:
            flag = False
            ans = 'mixed'


print(ans)