import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline().strip())

    if n >= 1 and n <= pow(10, 5):
        registration_counts = defaultdict(int)

        for _ in range(n):
            name = sys.stdin.readline().strip()

            if len(name) >= 1 and len(name) <= 32:
                if registration_counts[name] == 0:
                    print("OK")
                else:
                    print(f'{name}{registration_counts[name]}')
                # fim else
            # fim if

            registration_counts[name] += 1
        # fim for
    # fim if
# fim def

if __name__ == "__main__":
    main()
# fim if
