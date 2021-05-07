// 2016년
// 2016년 a월 b일은 무슨 요일일까요 ? 두 수 a, b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.
function solution(a, b) {
    var answer = '';
    var sum = 0;
    var months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];

    function sumMonths(a) {
        if (a === 0) return 0;
        return months.slice(0, a - 1).reduce(function (acc, cur) {
            return acc + cur;
        })
    }

    function findDay() {
        for (var i = 0; i < days.length; i++) {
            return days[sum % 7]
        }
    }

    var month = sumMonths(a);
    sum = month + b;
    answer = findDay();

    return answer;
}
// 배열의 값을 하나의 값으로 합칠 때, reduce 메소드 사용