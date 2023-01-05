import queue

b = queue.Queue()

b.put(0)  # 데이터를 추가하기 위해서는 put 함수를 사용한다.
b.put(1)

print(b.get())  # 데이터를 제거할때 사용하는 함수
print(b.qsize())  # q의 사이즈를 측정 하는 함수

a = queue.LifoQueue()
a.put(0)
a.put(1)
a.put(2)

print(a.get())  # 마지막 원소의 값

print(a.qsize())  # 큐의 사이즈

c = queue.PriorityQueue()

# c.put((우선순위 , data))
c.put((1, 0))
c.put((2, 1))
c.put((3, 2))

print(f'우선순위 값 : {c.get()[0]}, 데이터 값 : {c.get()[1]}')

print(c.qsize())  # 큐의 사이즈 측정
