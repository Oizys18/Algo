class Queue {
  constructor() {
    this.data = [];
  }

  enqueue(item) {
    this.data.push(item); // data의 오른쪽에 data push
  }
  dequeue() {
    if (this.data.length === 0) {
      return "Queue is empty";
    }
    return this.data.shift(); // 왼쪽으로 shift, [0]의 데이터를 pop
  }
  length() {
    return this.data.length;
  }
  peek() {
    if (this.data.length === 0) {
      return "Queue is empty";
    }
    return this.data[0];
  }
  isEmpty() {
    if (this.data.length > 0) {
      return false;
    }
    return true;
  }
  clear() {
    this.data = [];
  }
}

// const q = new Queue();
// const log = console.log;
// log(q);
// q.enqueue(1);
// q.enqueue(2);
// q.enqueue(3);
// log(q.peek());
// log(q.length());
// log(q.isEmpty());
// q.clear();
// log(q.isEmpty());
// log(q.length());
// q.enqueue(1);
// q.enqueue(3);
// q.enqueue(5);
// log(q);
// q.dequeue();
// q.dequeue();
// log(q);
