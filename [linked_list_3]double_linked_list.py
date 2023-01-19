class Node:
    def _init_(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Nodemanage:
    def _init_(self,data):
        self.head = Node(data) # Nodemanage(data)라고 선언하면 맨 처음이 만들어 지는 것
        self.tail = self.head  # Node의 객체로서 선언될 당시에 data,prev,next를 가지게 되고, 그 상위 단계에서 tail, head 의 개념을 가지게 된다.
    
    def insert(self,data):
        # 마지막까지 탐색 후 Node(data)라는 객체를 마지막에 추가한다.
        if self.head == None:
            self.head = Node(data) # 방어코드 즉 Nodemanage(data) 형식의 객체가 선언되지 않았을때 쓰는 것
            self.tail = self.head
        else:
            node = self.head 
            while node.next:
                node = node.next
            new = Node(data) # Node 객체를 선언 할 당시에는 data 만이 아닌 prev과 next또한 설정해 주어야 한다!
            # tail과 next 설정은 Node(data,prev,next)로 설정할 수도 있지만 반대로 그냥 Node(data)로 선언되어서 prev, next 모두 None 으로 설정된 상태에서 
            # 머시기.prev, 머시기.next로 설정할 수도 있다
            # 따라서 new 는 추가되는 거라 next야 어차피 None이라서 상관할 필요가 없고 , prev는 대신 설정을 해 주어야 한다.
            new.prev = node
            node.next = new # 원래 none 이었던 항목을 Node(data)라는 insert할 항목의 주소로 바꾼다
            self.tail = new
