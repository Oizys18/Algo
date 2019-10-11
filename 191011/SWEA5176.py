import sys
sys.stdin= open('input2.txt','r')

# def BST(start):
#     node = start
#     binTree[node] = [node+1,,node+2]



def inorder(node):
    global cnt 
    if node > N:
        
        return  
    else:
        inorder(node*2)
        cnt += 1
        if node == int(N/2):
            arr[1] = cnt   
        if node == 1:
            arr[0] = cnt 
        inorder(node*2 + 1)    





for T in range(int(input())):
    N = int(input())
    arr = [0,0]
    cnt = 0
    inorder(1)
    print(f"#{T+1} {arr[0]} {arr[1]}")