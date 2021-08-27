"""
프린터
문제 설명
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
입출력 예
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
입출력 예 설명
예제 #1

문제에 나온 예와 같습니다.

예제 #2

6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.

출처
"""
def solution(priorities, location):
    que = [(idx,val) for (idx,val) in enumerate(priorities)]
    answer = 0
    while True:
        J = que.pop(0)
        if any(J[1] < item[1] for item in que):
            que.append(J)
        else:
            answer += 1
            if J[0] == location:
                return answer

# while루프와 for 루프를 사용해서 풀었다. 
# for로 J보다 우선도가 높은 문서를 찾아서, 
# 1. 우선도가 높은 문서가 없다:
#   1-1. 현재 location이 0이다(출력하려는 문서다)면 return answer 
#   1-2. 아니라면 location -= 1 (한 문서가 인쇄되었으므로) answer += 1  
# 2. 우선도가 높은 문서가 있다:
#   2-1. 현재 location이 0이다 : location += len(priorities)+1
#   2-2. 아니라면 location -= 1 

# 이렇게 푼 이유는 location값이 priorities를 pop할 때마다 달라지기 때문이라고 생각했기 때문이다. 
# 그런데 다른 사람 풀이 중에서 제일 처음에 enumerate를 통해 최초 리스트 상태에서 idx 값을 저장하는 방식을 확인했다. 
# 또한 python의 any함수를 처음 봤다. any는 주어진 값에 하나라도 True가 나오면 True를 반환하는 함수다. 
# any함수 안에 for 문을 list comprehension으로 돌려서 코드를 간소화할 수 있었다. 
# * any는 built_in module에 포함된 function이다. (하나라도 True면 True, 빈 배열은 False)
