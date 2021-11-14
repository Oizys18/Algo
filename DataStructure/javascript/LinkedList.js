// https://velog.io/@kimkevin90/Javascript%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Linked-List-%EA%B5%AC%ED%98%84
class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }
  insertFront(data) {
    this.head = new Node(data, this.head);
    this.size++;
  }
  insertLast(data) {
    let node = new Node(data);
    let current;

    // if empty, make head
    if (!this.head) {
      this.head = node;
    } else {
      current = this.head;

      while (current.next) {
        //this.head에 next가 있다면 즉, next가 null이아니라면
        current = current.next; // current는 current.next가 되고
      }

      current.next = node; //결국 current.next가 새로넣은 node가 된다?
    }
    this.size++; //length 는 1증가
  }
}

class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}
