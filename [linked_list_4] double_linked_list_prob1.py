# 구현할 기능 : 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수 만들기
# 더블 링크드 리스트의 tail 에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
# 테스트 : 임의로 0~9까지 데이터를 링크드 리스트에 넣어보고 , 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드 추가하기

class Node:
    def _init_(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Nodemanage:
    def _init_(self,data):
        self.head = Node(data) # 새로 만들어 주는 기능까지 가짐
        self.tail = self.head 

    def insert(self,data):
        if( self.head == "" ): # 방어코드
            self.head = Node(data) # 맨 앞의 아이니까 prev도 None일 거고, next도 None 일거다 따라서 아무것도 건드리지 않는다.
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            new.prev = node
            node.next = new # None 값을 new = Node(data) 의 주소 값으로 바꿈
            self.tail = new
            # 하위차원 --> Node 객체(data,prev,next 소유) 와 # 상위차원 --> Nodemanage 객체 (head,tail 소유) 를 분리 해야함

    def desc(self):
        node = self.head # 사실상 안 바뀌지
        while node.data :
            print(node.data)
            node = node.next

# 구현할 기능_1 

    def resume(finding_data,new_data):
        node = self.head # node 는 self 축의 객체 인 동시에 어쨋든 Node로 선언된 객체이기에 prev와 next가 존재하는 친구이다. 
        # 분명 resume 함수를 구현하기 전에 insert 함수를 이용했을 거고 그로 인해 self.tail 이 잘 설정되어 있을 것이다.
        # 그러나 혹시 모를 상황을 대비해 self.tail 재설정 함수를 만든다.
        while node.next:
            node = node.next # tail 찾기
        self.tail = node # 재설정 함수의 끝 현재 node의 값은 tail객체
        new = Node(new_data) 
        while node.prev:  # tail 에서부터 조사를 시작하개 하는 구문
            if node.data == finding_data: # 이 친구에서 prev를 바꿔준다.
                tempo_prev = node.prev # 나중에 node_prev 값 바꿀거니까 미리 설정해 놓아야 한다.
                new.prev = tempo_prev
                new.next = node
                node.prev = new
            else:
                node = node.prev

# 테스트
        node0 = nodemanage(0)

        for insert_data in range(1,10):
            node0.insert(insert_data)

        node0.resume(3,2.5)

        print(node0)
