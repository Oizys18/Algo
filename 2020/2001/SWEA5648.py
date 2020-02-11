# 원자소멸


dr = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    # Get Initial Atom Infos
    curr_atom = {}
    for _ in range(N):
        x, y, direc, K = map(int, input().split())
        curr_atom[(x, y)] = [direc, K]

    # 턴 진행
    res_energy = 0
    next_atom = {}
    while True:
        dead_atom = set()

        # move atoms and collide
        for key, value in curr_atom.items():
            x, y = key
            dx, dy = dr[curr_atom[key][0]]
            nx, ny = x + dx, y + dy
            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:    
                if next_atom.get((nx, ny)):
                    dead_atom.add((nx, ny))
                    next_atom[(nx, ny)][1] += curr_atom[key][1]
                else:
                    next_atom[(nx, ny)] = value
        if len(dead_atom):
            for x,y in dead_atom:
                res_energy += next_atom.pop((x,y))[1]
        curr_atom = next_atom.copy()
        next_atom = {}
        if len(curr_atom) == 0:
            break

    print(f"#{testcase} {res_energy}")