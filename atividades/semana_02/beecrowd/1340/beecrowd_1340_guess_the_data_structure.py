import sys, heapq
from collections import deque

def main():
    n = sys.stdin.readline().strip()

    while n is not None and n != "":
        n = int(n)
        isStack = isQueue = isPriorityQueue = True
        stack = []
        queue = deque([])
        priorityQueue = []

        for _ in range(n):
            operation, value = map(int, sys.stdin.readline().strip().split())
            if operation == 1:
                stack.append(value)
                queue.append(value)
                heapq.heappush(priorityQueue, -value)
            elif operation == 2:
                if isStack:
                    if stack.pop() != value:
                        isStack = False
                    # fim if
                # fim if
                if isQueue:
                    if queue.popleft() != value:
                        isQueue = False
                    # fim if
                # fim if
                if isPriorityQueue:
                    if heapq.heappop(priorityQueue) != -value:
                        isPriorityQueue = False
                    # fim if
                # fim if
            # fim elif
        # fim for

        if sum([isStack, isQueue, isPriorityQueue]) > 1:
            print("not sure")
        elif isStack:
            print("stack")
        elif isQueue:
            print("queue")
        elif isPriorityQueue:
            print("priority queue")
        else:
            print("impossible")
        # fim else

        n = sys.stdin.readline().strip()
    # fim while
# fim def

if __name__ == "__main__":
    main()
# fim if
