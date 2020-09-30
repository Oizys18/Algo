var fs = require('fs');
let array = fs.readFileSync('/dev/stdin').toString().split('\n');
let N = array[0];
mat = new Array(N)
for (let i = 0; i < N ; i++) {
    mat[i] = new Array(3)
    for (let j = 0; j < 3; j++) {
        mat[i][j] = Number(array[i+1].split(' ')[j])
    }
}

let DP = new Array(N)
for (let i = 0; i < N; i++) {
    DP[i] = [0, 0, 0]
}
DP[0] = mat[0]

for (let h=1; h < N; h++){
    DP[h][0] = Math.min(DP[h-1][1],DP[h-1][2]) + mat[h][[0]]
    DP[h][1] = Math.min(DP[h-1][0],DP[h-1][2]) + mat[h][[1]]
    DP[h][2] = Math.min(DP[h-1][0],DP[h-1][1]) + mat[h][[2]]
}
console.log(Math.min(...DP[N-1]))