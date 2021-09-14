from collections import defaultdict
def solution(arrows):
    answer = 0
    dr = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    graph = defaultdict(set)
    visit = set()
    visit.add((0,0))
    x,y = 0,0
    
    """
    사각형 만들어지는 조건 
    (이전에 그리지 않은 선으로)
    1. 방문했던 점을 다시 방문
    2. 대각선으로 교차함 
    """
    for arrow in arrows: 
        nx,ny = x+dr[arrow][0],y+dr[arrow][1]
        if (nx,ny) in visit and (nx,ny) not in graph[(x,y)] :
            answer += 1 
        if (nx,ny) not in graph[(x,y)] and arrow in [1,3,5,7]:
            if arrow == 1:
                dotA = (x+dr[2][0], y+dr[2][1])
                dotB = (x+dr[0][0], y+dr[0][1])
            elif arrow == 3:
                dotA = (x+dr[2][0], y+dr[2][1])
                dotB = (x+dr[4][0], y+dr[4][1])
            elif arrow == 5:
                dotA = (x+dr[4][0], y+dr[4][1])
                dotB = (x+dr[6][0], y+dr[6][1])
            elif arrow == 7:
                dotA = (x+dr[6][0], y+dr[6][1])
                dotB = (x+dr[0][0], y+dr[0][1])
            if dotA in graph[dotB]:
                answer += 1 
        visit.add((nx,ny))
        graph[(x,y)].add((nx,ny))
        graph[(nx,ny)].add((x,y))
        x,y = nx,ny 
    return answer

"""
풀이 보고 도움 받았다. 
graph를 그리는 것까지는 옳았는데, 해당 그래프를 이용할 방법을 생각해내지 못했다. 

결국 중요한 건 방이 만들어지는 조건을 판별하고, 새로운 방이 생성될 때마다 체크해주는 것이다. 

방이 생성되려면 이전에 그려지지 않은 선분으로 (중복선분금지)
1. 이전에 방문한 점을 재방문 
2. 다른 대각선 대각선으로 교차함 

2번의 경우 arrow의 방향에 따라 각각의 경우 X자로 생성되는 대각선이 이미 그려져 있는지를 체크해야한다. 

또한, 선분을 X->Y 만 체크하면 방향이 달라지면 못체크하니까 Y->X도 체크해야한다. 
"""


"""
다 풀고나서 풀이를 보니까 
오일러 다면체정리 있었다. 
https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%EB%8B%A4%EB%A9%B4%EC%B2%B4_%EC%A0%95%EB%A6%AC

3차원에서 v(vortex 꼭지점 개수) , e(edge 모서리 개수), f(face 면 개수)가 있으면 
v-e+f = 2가 항상 성립한다. 

2차원에서는 v-e+f=1 이 항상 성립하므로 
v 꼭지점 개수 (방문 점 개수)
e 모서리 개수 (선분 개수)

구한 후, 1-v+e를 계산하면 면의 갯수가 나온다. 


단, 이 방법으로 계산할 시 모든 선분의 중간지점 (1/2,1/2 등)을 계산해줘야 한다. 
x,y의 각각을 2로 나눠서 0.5 단위로 계산하던가, 모든 선분을 *2해서 계산해야한다. 
"""
def solution2(arrows):
    dirs = [ (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1) ]
    vertex = set()
    edge = set()
    (x, y) = (0, 0)
    vertex.add((x, y))

    for arrow in arrows:
        for _ in range(2): # 모든 좌표를 2번씩 더해서, 선분이 2칸씩 이동한다(1/2 좌표계산과 동일한 효과)
            (nx, ny) = ( x + dirs[arrow][0], y + dirs[arrow][1] )
            if (x,y)>(nx,ny): edge1,edge2 = (x, y),(nx, ny)
            else: edge2,edge1 = (x, y),(nx, ny)

            vertex.add((nx, ny))
            edge.add((edge1,edge2))
            (x, y) = (nx, ny)

    return 1-len(vertex)+len(edge)

    
def solution3(arrows):
    point=set([(0,0)])
    line=set()
    move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]]
    pre_point=(0,0)
    for A in arrows:# mid_point 계산으로 중간지점 계산해줬다.
        next_point=(pre_point[0]+move[A][0],  pre_point[1]+move[A][1] )
        mid_point=(pre_point[0]+move[A][0]//2,  pre_point[1]+move[A][1]//2 )
        point.add(next_point)
        point.add(mid_point)
        line.add((pre_point,mid_point))
        line.add((mid_point,pre_point))
        line.add((mid_point,next_point))
        line.add((next_point,mid_point))
        pre_point=next_point
    answer = len(line)//2-len(point)+1
    return answer if answer>=0 else 0