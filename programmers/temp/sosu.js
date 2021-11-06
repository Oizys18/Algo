function solution(numbers) {
  const check = (n) => {
    if (n < 2) return false;
    for (let i = 2; i < Math.floor(Math.sqrt(n)) + 1; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  const permutator = (inputArr) => {
    let result = new Set();
    const arr = (inputArr) => {
      let temp = [];
      for (const i of inputArr) {
        temp.push(i);
      }
      return temp;
    };

    const permute = (arr, m = "") => {
      if (arr.length === 0) {
        result.add(Number(m));
      } else {
        for (let i = 0; i < arr.length; i++) {
          let curr = arr.slice();
          let next = curr.splice(i, 1);
          permute(curr.slice(), m + next);
          permute(curr.slice(), m);
        }
      }
    };
    permute(arr(inputArr));
    return result;
  };

  return Array.from(permutator(numbers)).filter((i) => check(i)).length;
}
