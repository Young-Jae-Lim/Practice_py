# def feat(n):
#     clu = 1
#     if n > 0:
#         clu = n * feat(n-1)
#     return clu

# if __name__ == "__main__":
#     A = int(input())
#     print(feat(A))

def feeboo(n):
    if n <= 1:
        return n
    return feeboo(n-1) + feeboo(n-2)

if __name__ == "__main__":
    A = int(input())
    print(feeboo(A))