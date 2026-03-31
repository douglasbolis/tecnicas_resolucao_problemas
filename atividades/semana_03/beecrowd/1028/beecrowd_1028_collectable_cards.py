import sys
from math import gcd

def main():
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(gcd(a, b))
    # fim for
# fim def

if __name__ == "__main__":
    main()
# fim if
