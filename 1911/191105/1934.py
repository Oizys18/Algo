for T in range(int(input())):
    a, b = map(int,input().split())
    A, B = max(a,b), min(a,b)
    def find(A, B):
        while True:
            r = A % B 
            if r == 0:
                return B
            else:
                A = B 
                B = r 
    print((A * B)//find(A, B))

"""
2609와 동일, 유클리드 호제법
"""