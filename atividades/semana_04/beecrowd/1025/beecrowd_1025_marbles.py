import sys

def main():
    n, q = list(map(int, sys.stdin.readline().strip().split()))
    cases = 0

    while n != 0 and q != 0:
        marbles = [None] * n
        queries = [None] * q

        print(f'CASE# {cases+1}')

        for i in range(n):
            marbles[i] = int(sys.stdin.readline().strip())
        # fim for

        for i in range(q):
            queries[i] = int(sys.stdin.readline().strip())
        # fim for

        marbles.sort()

        for i in queries:
            found = False
            j = 0

            while not found and j < len(marbles):
                if i == marbles[j]:
                    found = True
                # fim if

                j += 1
            # fim while

            print(f'{i} found at {j}') if found else print(f'{i} not found')
        # fim for

        n, q = list(map(int, sys.stdin.readline().strip().split()))
        cases += 1
    # fim while

if __name__ == "__main__":
    main()
# fim if
