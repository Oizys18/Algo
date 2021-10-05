def toSec(time : str)->int:
    h,m,s = time.split(':')
    hs = int(h)*3600
    ms = int(m)*60
    s = int(s)
    return hs+ms+s 
def num_to_time(num):
    hours = "0"+str(num//3600)
    minutes = "0"+str((num%3600) // 60)
    seconds = "0"+str((num%3600)%60)
    return ":".join([hours[-2:],minutes[-2:],seconds[-2:]])
    
def solution(play_time, adv_time, logs):
    answer = ''
    
    playT = toSec(play_time)
    advT = toSec(adv_time)
    logsT = [list(map(toSec,log.split('-'))) for log in logs]
    total = [0]*(playT+1)
    
    for start,end in logsT:
        total[start] += 1 
        total[end] -= 1
        
    for t in range(1,playT):
        total[t] += total[t-1]
        
    for t in range(1,playT):
        total[t] += total[t-1]
        
    mx = total[advT-1]              # 00:00:00 ~ ad 까지의 시청자 수
    time_large_view = 0
    for i in range(advT, playT):
        if mx < total[i]-total[i-advT]:
            mx = total[i]-total[i-advT]
            time_large_view = i+1 - advT
    return num_to_time(time_large_view)