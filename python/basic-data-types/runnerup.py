#!/bin/python3


if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(list(map(int, input().split()))))
    print(arr[-2])
