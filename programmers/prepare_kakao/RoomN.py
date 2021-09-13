from collections import defaultdict
def solution(arrows):
    answer = 0
    dr = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    graph = defaultdict(set)
    x,y = 0,0
    for arrow in arrows: 
        nx,ny = x+dr[arrow][0],y+dr[arrow][1]
        graph[(x,y)].add((nx,ny))
        graph[(nx,ny)].add((x,y))
        x = nx 
        y = ny 
    for k,v in graph.items():
        # 방 판별 필요 
        if len(v) >= 3:
            answer += 1
        
                

    return answer