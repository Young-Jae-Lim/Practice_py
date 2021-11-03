# def change(A):
#     if str(type(A)) == "<class 'int'>":
#         print(chr(A))
#     elif str(type(A)) == "<class 'str'>":
#         print(ord(A))

# if __name__ == "__main__":
#     A = input()
#     change(A)

import sys
A = int(input())
B = list(map(str, sys.stdin.readline()))
if A != (len(B)-1):
    None
else:
    B = [int(i) for i in B[:A]]
    print(sum(B))
