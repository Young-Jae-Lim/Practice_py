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

# import sys
# B = list(map(str, sys.stdin.readline()))
# count = []
# for i in range(26):
#     count.append(-1)
# for j in range(len(B)-1):
#     check = ord(B[j])-97
#     if (check) >= 0:
#         if count[check] == -1:
#             count[check] = j
# for z in range(26):
#     print(count[z],end=' ')

# import sys
# A = int(input())
# save = []
# for i in range(A):
#     B = list(map(str, sys.stdin.readline()))
#     for j in B[2:(len(B)-1)]:
#         for z in range(int(B[0])):
#             save.append(j)
#     print(''.join(save))
#     save.clear()
#join함수를 사용하면 리스트에 있는 string타입의 각각의 요소를 합쳐서 하나의 문자열로 만듬


# import sys
# B = list(map(str, sys.stdin.readline()))
# B .remove('\n')
# B = [i.replace(i,i.upper()) for i in B]
# count = []
# for i in range(26):
#     count.append(0)
# for j in B:
#     check = ord(j) - 65
#     count[check] +=1
# if count.count(max(count)) > 1:
#     print('?')
# else:
#     max = count.index(max(count))
#     print(chr(max+65))

# import sys
# B = list(map(str, sys.stdin.readline().split()))
# print(len(B))

# import sys
# B = list(map(int, sys.stdin.readline().split()))
# save = []
# for i in B:
#     hun = i // 100
#     ten = (i % 100) // 10
#     one = i % 10
#     save.append((one * 100) + (ten * 10) + (hun))
# print(max(save))

# import sys
# num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# sec = 0
# B = list(map(str, sys.stdin.readline()))
# B.remove('\n')
# B = [i.replace(i,i.upper()) for i in B]

# for i in B:
#     for j in num:
#         if i in j:
#             sec += num.index(j)+3

# print(sec)

# import sys
# cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# count = 0
# A = sys.stdin.readline()
# for i in cro_alpha:
#     if i in A:
#         A = A.replace(i,"*")
# print(len(A)-1)

import sys
A = int(input())
count = A
for i in range(A):
    B = list(map(str, sys.stdin.readline()))
    for j in range(len(B)-1):
         if B[j] == B[j+1]:
             pass
         elif B[j] in B[j+1:]:
             count -=1
             break
print(count)