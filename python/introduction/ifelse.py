#!/bin/python3


if __name__ == '__main__':
    n = int(input().strip())

    print("Weird" if (n%2 != 0 or (n%2 ==0 and n in range(6, 21))) else "Not Weird")
