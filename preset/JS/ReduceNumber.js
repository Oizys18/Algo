// 같은 숫자는 싫어
// 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
// 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
function solution(arr) {
    let unique_array = []
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== arr[i + 1]) {
            unique_array.push(arr[i])
        }
    }
    return unique_array;
}
// 배열 안에 중복되는 value값을 제거(includes, indexOf…)
// 배열 안에 중복되는 value값이 몇 개인지 확인(object)