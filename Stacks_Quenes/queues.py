# Queues (FILO)

from collections import deque
que = deque()
print(que)

#enqueue, helps to add into the queue, append(), time: o(1)

que.append(2)
que.append(4)
que.append(5)
print(que)

#Dequeue, remove from the first side, popleft() time: o(n)
remove = que.popleft()
print(remove)
