```
파이썬과 로직이 동일했지만, 
JS의 sort()는 아스키코드 기준 비교라서 
numeric array를 단순 sort()하면 
1,10,11,2,3, ...
처럼 숫자 크기로 정렬되지 않는다. 

```
function solution(citations) {
    var answer = 0;
    citations = citations.sort(function(a,b){return a-b})
    for (let idx=0; idx <citations.length+1; idx++){
        if (citations[idx] >= citations.slice(idx).length){
            answer = citations.slice(idx).length
            break
        }
    }
    return answer;
}

