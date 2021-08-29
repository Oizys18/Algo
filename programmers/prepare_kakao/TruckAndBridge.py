def solution(bridge_length, weight, truck_weights):
    time = 0
    N = len(truck_weights)
    burden = 0
    crossed = 0 
    bridge = [] 
    while crossed < N:
        if bridge:
            if bridge[0][1] == time:
                truck, costed = bridge.pop(0)
                burden -= truck 
                crossed += 1 
        if truck_weights:
            if burden + truck_weights[0] <= weight and len(bridge) < bridge_length:
                truck = truck_weights.pop(0)
                burden += truck 
                bridge.append([truck,time+bridge_length])
        time += 1 
    return time



"""
# Line 7에서 while에 or로 다리에 남아있는 트럭 or 대기중인 트럭을 넣어줘서, 남은 트럭 체크할 변수사용을 줄일 수 있었다. 

def solution(bridge_length, weight, truck_weights):
    time = 0
    burden = 0
    bridge = [] 
    while bridge or truck_weights:
        if bridge:
            if bridge[0][1] == time:
                truck, costed = bridge.pop(0)
                burden -= truck 
        if truck_weights:
            if burden + truck_weights[0] <= weight and len(bridge) < bridge_length:
                truck = truck_weights.pop(0)
                burden += truck 
                bridge.append([truck,time+bridge_length])
        time += 1 
    return time
"""