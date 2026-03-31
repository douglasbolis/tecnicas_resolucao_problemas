import sys

def main():
    n = int(sys.stdin.readline().strip())
    degrees = []

    for _ in range(n):
        a = int(sys.stdin.readline().strip())
        degrees.append(a)
    # fim for
    
    for bitmask in range(1 << n):
        soma = 0

        for i in range(n):
            if bitmask & (1 << i):
                soma += degrees[i]
            else:
                soma -= degrees[i]
            # fim else
        # fim for

        if soma % 360 == 0:
            print("YES")
            return
        # fim if
    # fim for

    print("NO")
# fim def

if __name__ == "__main__":
    main()
# fim if
