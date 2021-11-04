from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = defaultdict(list)
        point = 0
        flag = 0
        for w in s:
            rows[point].append(w)
            if flag:
                point -= 1
            else:
                point += 1
                if point == numRows-1:
                    flag = 1
            if point == 0:
                flag = 0

        return ''.join([''.join(i) for i in rows.values()])


""" 
dict를 사용해서 풀었다. 
지그재그로 이동하는 포인터를 사용했다.
0에서 시작한 point는 
1. 1씩 증가한다. 
2. numRows에 도달하면 flag를 세우고 point를 줄인다. 
3. 다시 0에 도달하면 flag를 내리고 point를 증가시킨다. 

* numRows == 1 인 엣지케이스를 해결하지 않아서 한 번 FAIL 했었다. 
"""
