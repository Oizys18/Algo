const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString();
const N = parseInt(input);

let answer = "";
for (let i = 1; i <= N; i++) {
  answer += i + "\n";
}
console.log(answer);
