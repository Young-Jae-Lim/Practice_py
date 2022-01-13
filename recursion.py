# def feat(n):
#     clu = 1
#     if n > 0:
#         clu = n * feat(n-1)
#     return clu

# if __name__ == "__main__":
#     A = int(input())
#     print(feat(A))

# def feeboo(n):
#     if n <= 1:
#         return n
#     return feeboo(n-1) + feeboo(n-2)

# if __name__ == "__main__":
#     A = int(input())
#     print(feeboo(A))


# def star(n, list):
#     all_star = []
#     if n == 3:
#         return list
#     else:
#         for i in list:
#             all_star.append(i * 3)
#         for i in list:
#             all_star.append(i + " " *len(list) + i)
#         for i in list:
#             all_star.append(i*3)
#         return star(n//3,all_star)
    
# if __name__ == "__main__":
#     A = int(input())
#     first_start = ["***", "* *", "***"]
#     all = star(A,first_start)
#     for i in all:
#         print(i)
        
# #참고 : https://imgzon.tistory.com/37

def hanoi(n,start,tmp,end):
    if n == 1:
        print(start,end)
    else:
        hanoi(n-1,start,end,tmp)
        print(start,end)
        hanoi(n-1,tmp,start,end)

if __name__ == "__main__":
    A = int(input())
    print((2**A)-1)
    hanoi(A,1,2,3)