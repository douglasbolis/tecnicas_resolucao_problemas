import sys

def main():
    w = int(sys.stdin.readline().strip())

    if w > 3 and w % 2 == 0:
        print("YES")
    else:
        print("NO")
    # fim else
# fim def

if __name__ == "__main__":
    main()
# fim if

