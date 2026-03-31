import sys
from math import isqrt

def main():
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        a = int(sys.stdin.readline().strip())
        isPrime = True

        if a < 2:
            isPrime = False
        else:
            for i in range(3, isqrt(a) + 1, 2):
                if a % i == 0:
                    isPrime = False
                    break
                # fim if
            # fim for
        # fim else

        if isPrime:
            print("Prime")
        else:
            print("Not Prime")
        # fim else
    # fim for
# fim def

if __name__ == "__main__":
    main()
# fim if
