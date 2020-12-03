function solution(n, lost, reserve) {
    var answer = 0;
    let cloth = new Array(n).fill(1)
    lost.forEach(i => cloth[i - 1] = 0)
    for (let j = 0; j < reserve.length; j++) {
        if (cloth[reserve[j] - 1] == 0) {
            cloth[reserve[j] - 1] = 1
            reserve.splice(j, 1)
        }
    }
    console.log(reserve)
    for (let k = 0; k < reserve.length; k++) {
        if (reserve[k] - 2 >= 0 && cloth[reserve[k] - 2] == 0) {
            cloth[reserve[k] - 2] = 1
        } else if (reserve[k] <= n - 1 && cloth[reserve[k]] == 0) {
            cloth[reserve[k]] = 1
        }
    }

    function sum(pre, nxt) {
        return pre + nxt
    }
    return cloth.reduce(sum)

}