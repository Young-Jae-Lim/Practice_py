# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = int(sys.stdin.readline())
#     save.append(B)
# for i in range(len(save)):
#     min1 = min(save)
#     print(min1)
#     save.remove(min1)
    
# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = int(sys.stdin.readline())
#     save.append(B)
# save.sort()
# for i in save:
#     print(i)

# import sys
# A = int(sys.stdin.readline())
# check = [0] * 10001
# for i in range(A):
#     check[int(sys.stdin.readline())]+=1
# for i in range(10001):
#     if check[i]!=0:
#         for j in range(check[i]):
#             print(i)
# #참고: https://pacific-ocean.tistory.com/67

# import sys
# from collections import Counter
# A= int(sys.stdin.readline())
# save = []
# for i in range(A):
#     save.append(int(sys.stdin.readline()))
# save.sort()
# print(round(sum(save)/A))
# print(save[A//2])
# save_count = Counter(save).most_common()
# if len(save_count) > 1:
#     if save_count[0][1] == save_count[1][1]:
#         print(save_count[1][0])
#     else:
#         print(save_count[0][0])
# else:
#     print(save_count[0][0])        
# print(max(save)-min(save))
#참고: https://velog.io/@jaenny/%EB%B0%B1%EC%A4%80-2108-%ED%86%B5%EA%B3%84%ED%95%99-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC
#다시볼 필요가 있음 round, Count함수 알아둘것.

# import sys
# A = list(sys.stdin.readline())
# A.sort(reverse=True)
# A.remove('\n')
# print("".join(A))

# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = list(map(int, sys.stdin.readline().split()))
#     save.append(B)
# save.sort()
# for i in save:
#     print(str(i[0])+' '+str(i[1]))

# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = list(map(int, sys.stdin.readline().split()))
#     save.append(B)
# save.sort(key = lambda x:(x[1],x[0]))
# for i in save:
#     print(str(i[0])+' '+str(i[1]))
#lambda 참고: https://dev-note-97.tistory.com/13

# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = str(sys.stdin.readline())
#     save.append(B)
# save = list(set(save))
# save.sort(key = lambda x:(len(x), x))
# for i in save:
#     i = str(i).strip()
#     print(i)

# import sys
# A = int(sys.stdin.readline())
# save = []
# for i in range(A):
#     B = list(map(str, sys.stdin.readline().split()))
#     save.append(B)
# save.sort(key = lambda x:int(x[0]))
# for i in save:
#     print(i[0],i[1])

import sys
A = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
if len(B) > A:
    None
else:
    C = sorted(list(set(B)))
    dic = {C[i]:i for i in range(len(C))}
    for i in B:
        print(dic[i], end=' ')
#sorted로 객체 깊은 복사, 딕셔너리 이용하여 키값 및 값 지정하여 출력