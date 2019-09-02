# SWEA 5099 피자굽기 

"""
N 개의 피자 동시에 굽는 화덕
1~M 번까지 M개의 피자를 순서대로 화덕에 넣기 

치즈가 모두 녹으면 화덕에서 꺼냄
치즈의 양은 피자마다 다르다. 

마지막까지 남아있는 피자 번호를 알아내시오 
0. input 받기 
1. def oven():
    초기 : queue가 가득 찰 때까지 pizzas에서 pop(0)해서 queue에 넣기  
    - 원형 queue: 자동으로 계속 돌아감  while 
    dequeue해서 Cheese//2 한다음 값을 확인  
        if cheese == 0 :
            if pizzas가 비어있지 않다면! 
                뺀 자리에 pizzas에서 pop(0)해서 queue에 넣기
            if queue가 비어있는지 확인 
                만약 비어있다면 ( 방금 dequeue한게 마지막 값이라면)
                return 값  
        elif cheese != 0 :
            같은 자리에 다시 넣기 
"""
import sys
sys.stdin = open('input4.txt','r')

front = rear = 0
def cQ(pizzas):
    
    oven = [0] * (N + 1)
    def isEmpty():
        global front
        global rear
        return front == rear

    def isFull():
        global front
        global rear
        return (rear + 1) % len(oven) == front

    def enQueue(item):
        global rear
        if isFull():
            print("Queue full")
        else:
            rear = (rear + 1) % len(oven)
            # print(rear)
            oven[rear] = item

    def deQueue():
        global front
        if isEmpty():
            print("Queue empty")
        else:
            front = (front + 1) % len(oven)
            return oven[front]
    for _ in range(N):
        enQueue(pizzas.pop(0))
    while not isEmpty():
        idx, cheese = deQueue()
        cheese = cheese // 2
        if cheese == 0:
            if pizzas:
                pizza = pizzas.pop(0)
                enQueue(pizza)
            if isEmpty():
                return idx+1
        else:
            enQueue([idx,cheese])

for T in range(int(input())):
    N, M = map(int,input().split())
    line = list(map(int,input().split()))
    pizzas = []
    for i in range(len(line)):
        pizzas.append([i,line[i]])
    print("#{0} {1}".format(T+1,cQ(pizzas)))

            




    
