function solution(new_id) {
    const answer = new_id
        .toLowerCase() //1
        .replace(/[^\w-_.]/g, '') // 2
        .replace(/\.+/g, '.') // 3
        .replace(/^\.|\.$/g, '') // 4
        .replace(/^$/, 'a') // 5
        .slice(0, 15).replace(/\.$/g, '')
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}

// 참고
// 2번의 내 코드 
// .replace(/[^a-z0-9-_.]/gi, '') // 2
// /[\w]로 알파벳 + 숫자 포함인가봄 


//   5번의 내 코드, 위 처럼 /^$/ 로 공백 표현 가능 
// if (alter_id.length === 0) {
//     alter_id = 'a'
// }  


//  7번의 내 코드, but while 안 쓰고 표현 가능 
// while (alter_id.length <= 2) {
//     let w = alter_id.charAt(alter_id.length - 1)
//     alter_id = alter_id + w
// }

// 7번의 다른 코드 
//  return id.padEnd(3, id[id.length-1])
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/padEnd
// padend는 현재 문자열에 주어진 길이만큼 다른 문자열을 붙여서 새로운 문자열을 반환함 