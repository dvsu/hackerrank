#!/bin/python3


if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)

    # second lowest score
    secondLowest = sorted(set(scores))[1]
    
    # sort records alphabetically
    records.sort()
    
    nameList = [print(records[x][0]) for x in range(len(records)) if records[x][1] == secondLowest]