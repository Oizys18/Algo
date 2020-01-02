mat = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
    ]


for i in range(3):
    for j in range(3):
        if i < j :
            continue
        elif i == j :
            print(mat[i][j])
        elif i > j:
            print(mat[i][j])
        