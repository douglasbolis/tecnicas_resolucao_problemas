import sys, heapq
from math import pow

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    cashiers = list(map(int, sys.stdin.readline().strip().split()))
    clients = list(map(int, sys.stdin.readline().strip().split()))
    cashierHeap = []
    maxTime = 0

    if n < 1 or n > m or m > pow(10, 4) or len(cashiers) != n or len(clients) != m:
        return
    # fim if

    for i in range(n):
        heapq.heappush(cashierHeap, (0, i))
    # fim for

    for items in clients:
        freeTime, cashier = heapq.heappop(cashierHeap)
        consumedTime = cashiers[cashier] * items
        newFreeTime = freeTime + consumedTime
        maxTime = max(maxTime, newFreeTime)
        heapq.heappush(cashierHeap, (newFreeTime, cashier))
    # fim for

    print(maxTime)
# fim def

if __name__ == "__main__":
    main()
# fim if
