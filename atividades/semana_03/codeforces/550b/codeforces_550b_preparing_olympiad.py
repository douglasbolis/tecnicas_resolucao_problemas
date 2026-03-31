import sys

def main():
    n, l, r, x = map(int, sys.stdin.readline().strip().split())
    problems = list(map(int, sys.stdin.readline().strip().split()))
    count = 0

    for mask in range(1 << n):
        k = mask.bit_count()
        if k < 2:
            continue
        # fim if

        total = 0
        min_val = 10**18
        max_val = -10**18

        for i in range(n):
            if mask & (1 << i):
                total += problems[i]
                min_val = min(min_val, problems[i])
                max_val = max(max_val, problems[i])
            # fim if
        # fim for

        if l <= total <= r and max_val - min_val >= x:
            count += 1
        # fim if
    # fim for

    print(count)
# fim def

if __name__ == "__main__":
    main()
# fim if
