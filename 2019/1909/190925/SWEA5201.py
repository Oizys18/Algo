import sys
sys.stdin = open('input3.txt','r')

for T in range(int(input())):
    N, M = map(int,input().split())
    
    container = sorted(list(map(int,input().split())))
    truck = sorted(list(map(int,input().split())))

    moved = 0
    for i in range(N):
        if truck:
            if max(container) <= max(truck):
                moved += container.pop()
                truck.pop()
            else:
                container.pop()
    print("#{} {}".format(T+1,moved))
            