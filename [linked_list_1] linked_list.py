class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

node1=Node(1)
node2=Node(2)
node1.next=Node(2) # 대입연산자의 우변이 클래스면 그 클래스의 
#주소가 들어가는 거니까 
head=node1

# 링크드 리스트로 데이터 추가
# 기능 : head = node1 로 설정된 출발점으로부터 node.next= NONE인 부분까지 가서
# 그 부분의 next를 다음에 이어 붙일 node로 연결 시키기

def add(data): 

    head=node1

    while head.next != None: # 즉 while node.next
        head=head.next
    
    head.next = Node(data) # 이건 즉 자신의 data의 내용이 data인 어떤 Node를 추가하는 것


# 기능 : node의 데이터의 내용이 data가 range(2,10) 인 node로 node 객체 확장시키기

for index in range(2,10):
    add(index)

while head.next: # while head.next != None
    print(head.data)
    head = head.next

print(head.data) # 마지막은 none이라는 얘기니까
