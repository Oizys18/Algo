class Stack {
  constructor() {
    this.data = [];
  }
  push(item) {
    this.data.push(item);
  }
  pop() {
    if (this.data.length === 0) {
      return "Stack is Empty";
    }
    return this.data.pop();
  }
  length() {
    return this.data.length;
  }
  peek() {
    if (this.data.length === 0) {
      return "Stack is Empty";
    }
    return this.data[this.data.length - 1];
  }
  isEmpty() {
    if (this.data.length === 0) {
      return true;
    }
    return false;
  }
  clear() {
    this.data = [];
  }
}
const s = new Stack();
const log = console.log;
log(s); // Stack { data: [] }
s.push(1);
s.push(2);
s.push(3);
log(s.peek()); // 3
log(s.length()); // 3
log(s.isEmpty()); // false
s.clear();
log(s.isEmpty()); // true
log(s.length()); // 0
s.push(1);
s.push(3);
s.push(5);
log(s); // Stack { data: [ 1, 3, 5 ] }
s.pop();
s.pop();
log(s); // Stack { data: [ 1 ] }
