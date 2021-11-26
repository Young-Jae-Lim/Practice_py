import sys
A = int(input())
B = list(map(int, sys.stdin.readline().split()))
count = 0
if A != len(B):
    None
else:
    for i in B:
        set = 0
        if i == 0:
            continue
        for j in range(2, i+1):
            if i % j == 0:
                set +=1
        if set == 1:
            count+=1
    print(count)