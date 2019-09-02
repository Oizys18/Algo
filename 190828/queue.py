# myQueue /// 선형 1차형 큐
N = 5
Q = [0] * N
front = rear = -1

def enQueue(item):
    global rear
    if isFull():
        print("Queue_full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1
        return Q[front]

def isEmpty():
    return front == rear
def isFull():
    return rear == len(Q) - 1

