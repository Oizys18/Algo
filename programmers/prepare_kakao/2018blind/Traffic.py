def toSec(time:str) -> int:
    h,m,s = time.split(':')
    h = int(h)*60*60*1000
    m = int(m)*60000
    s = int(float(s)*1000)
    return h+m+s
    
def solution(lines):
    answer = 0
    mx = toSec('23:59:59.999')
    temp = []
    for line in lines:
        date,start,duration = line.split()
        start = toSec(start)
        duration = int(float(duration[:-1])*1000)
        temp.append((start,min(start+duration,mx)))
    temp.sort()
    mn = temp[0][0]
    temp = [(i[0]-mn,i[1]-mn) for i in temp]
    print(temp)
    check=[0]*(temp[-1][1]-temp[0][0]+1)
    for du in temp:
        for t in range(du[0],du[1]+1):
            check[t] += 1 
    print(max(check))
    return answer

"""1초구간을 체크해야한다.."""