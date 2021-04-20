#!/bin/python3


def cmdList(command, numList):
    if command[0] == 'insert':
        numList.insert(int(command[1]), int(command[2]))
    elif command[0] == 'remove':
        numList.remove(int(command[1]))
    elif command[0] == 'append':
        numList.append(int(command[1]))
    elif command[0] == 'sort':
        numList.sort()
    elif command[0] == 'pop':
        numList.pop()
    elif command[0] == 'reverse':
        numList.reverse()

    return numList


if __name__ == '__main__':
    N = int(input())

    numList = []
    for _ in range(N):
        command = input().split()
        if command[0] != 'print':
            numList = cmdList(command, numList)
        else:
            print(numList)
