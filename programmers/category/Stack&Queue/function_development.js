// Progremmers 기능개발
progresses = [93,30,55]
speeds = [1,30,5]
function solution(progresses, speeds) {
    var answer = []
    let time = 0
    let count = 0
    while (progresses.length) {
        if (progresses[0] + speeds[0] * time >= 100) {
            progresses.shift()
            speeds.shift()
            count += 1
        } else {
            if (count > 0){
                answer.push(count)
                count = 0;
            }
            time += 1
        }
    }
    answer.push(count)
    return answer;
}
console.log(solution(progresses, speeds))