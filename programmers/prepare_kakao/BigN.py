def solution(number, k):
    answer = ''
    end = len(number) - k
    p = 0
    check = 0
    temp = []
    while len(temp) != end:
        big = '0'
        for i in range(p,p+k+1): 
            if big < number[i]:
                big = number[i]
                check = i
                if number[i] == '9':
                    break
        
        
        if big =='0':
            check = p 
        temp.append(number[check])
        k -= check - p
        p = check + 1 
        # print(check,p,k)
    answer = ''.join(temp)
    return answer


#새로 푼 것, 시간초과 + 실패 
def solution(number, k):
    answer = ''
    while k>0:
        for i in range(len(number)):
            a = number[:i]+number[i+1:]
            if number < a:
                number = a
                break
        else:
            number = number[1:]
        k-=1 
    answer = number 
    return answer

# 다시 새로 푼 것 , 성공 
def solution(number, k):
    N = len(number)
    check=[0]*N

    for idx,num in enumerate(number):
        if k and num != '9': #여기서 '9'일 때 그냥 넘기는 코드 추가로 시간초과를 벗어남 
            for j in range(idx+1,min(idx+k+1,N)):
                if number[j] > num:
                    k -= 1
                    check[idx] = 1 
                    break
    if k:return number[:k+1] 
    return ''.join([number[i] for i in range(N) if not check[i]])     

# Line 56: 모두 같은 숫자일 경우를 생각하고 추가. 
# 처음에 여기서 number[k:]로 했었는데, 생각해보니 모두 같지 않고 9998이런 식으로 들어올 수도 있었다. 
# 이럴경우 56이전의 코드에서 처리가 안되기 때문에 잘라줘야하는데 만약 [k:]로 자르면 998이되고, [:k+1]로 자르면 999가 된다.
# 뒤에 오는게 작은 수라는 것을 염두에 두고 잘랐어야함   



"""
다른사람 코드를 보니 중간에 내가 생각했던 스택을 사용해서 푸는 코드가 많았다. 
스택으로 풀지 않은 이유는 append를 많이 사용하면 시간복잡도가 현재보다 더 걸릴 것 같아서였는데, 
막상 풀고나니 9 같은 경우를 잘 관리한다면 문제가 없었다. 

"""
def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])