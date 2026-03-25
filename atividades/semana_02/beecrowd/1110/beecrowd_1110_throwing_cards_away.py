import sys
from collections import deque

def main():
    n = int(sys.stdin.readline().strip())
    
    while n > 0 and n <= 50:
        cards = deque(range(1, n+1))
        discardedCards = deque([])
        remainingCard = 0

        while len(cards) > 1:
            discardedCards.append(cards.popleft())
            cards.append(cards.popleft())
        # fim while

        remainingCard = cards[0]

        print(f'Discarded cards: {", ".join(map(str, discardedCards))}')
        print(f'Remaining card: {remainingCard}')

        n = int(sys.stdin.readline().strip())
    # fim while
# fim def

if __name__ == "__main__":
    main()
# fim if
