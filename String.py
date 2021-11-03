# def change(A):
#     if str(type(A)) == "<class 'int'>":
#         print(chr(A))
#     elif str(type(A)) == "<class 'str'>":
#         print(ord(A))

# if __name__ == "__main__":
#     A = input()
#     change(A)

# import sys
# A = int(input())
# B = list(map(str, sys.stdin.readline()))
# if A != (len(B)-1):
#     None
# else:
#     B = [int(i) for i in B[:A]]
#     print(sum(B))

import sys
B = list(map(str, sys.stdin.readline()))
count = []
for i in range(26):
    count.append(-1)
for j in range(len(B)-1):
    check = ord(B[j])-97
    if (check) >= 0:
        if count[check] == -1:
            count[check] = j
for z in range(26):
    print(count[z],end=' ')