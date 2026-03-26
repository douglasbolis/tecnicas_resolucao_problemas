import sys

def main():
    n = int(sys.stdin.readline().strip())

    if n >= 1 and n <= 100:
        for _ in range(n):
            word = sys.stdin.readline().strip()

            if len(word) >= 1 and len(word) <= 100:
                if len(word) <= 10:
                    print(word)
                else:
                    print(f'{word[0]}{len(word)-2}{word[-1]}')
                # fim else
            # fim if
    # fim if
    # fim for
# fim def

if __name__ == "__main__":
    main()
# fim if
