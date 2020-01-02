import sys
sys.stdin = open('5653.txt','r')
from pprint import pprint as pp

for T in range(int(input())):
    N, M, K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    deact = dict()
    act = dict()
    ready = dict()
    dead = dict()
 
    for x in range(N):
        for y in range(M):
            if mat[x][y]:
                deact[(x,y)] = [mat[x][y],mat[x][y]]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    # K 만큼 반복 
    for k in range(K):
        rm_ac = []
        for ac in act.keys():
            x,y = ac
            life = act[ac][0]
            time = act[ac][1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if dead.get((nx,ny)) or deact.get((nx,ny)) or act.get((nx,ny)):
                        continue
                else:
                    if not ready.get((nx,ny)):
                        ready[(nx,ny)] = [life,life]
                    else:
                        if ready[(nx,ny)][0] < life:
                            ready[(nx,ny)] = [life,life]
            act[ac][1] -= 1
            if act[ac][1] == 0:
                dead[ac] = 1
                rm_ac.append(ac)

        for rm in rm_ac:
            act.pop(rm)

        dc_rm = []
        for dc in deact.keys():
            deact[dc][1] -= 1
            if deact[dc][1] == 0:
                life = deact[dc][0]
                if not act.get(dc):
                    act[dc] = [life,life]
                dc_rm.append(dc)
        for rm in dc_rm:
            deact.pop(rm)
    
        deact.update(ready)
        ready = dict()

    print(f"#{T+1} {len(deact) + len(act)}")