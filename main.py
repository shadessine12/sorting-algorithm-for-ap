import pygame

#Credit to Geeks for Geeks Website for pseudocode on how to do selection sort
def selectionSort(list):
    for i in range(0, len(list)):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[minIndex], list[i] = list[i], list[minIndex]
    return list


def bubbleSort(list):
    while order(list) == false:
        for i in range(0, len(list)):
            if list[i] > list[i + 1]:
                list.insert(i, i + 1)
                list.pop(i + 2)
    return list


def order(list):
    truthCounter = 0
    for i in range(0, len(list)):
        if list[i] > list[i - 1] && list[i] < list[i + 1]:
            truthCounter = truthCounter + 1
    if truthCounter == len(list):
        return true 
    else:
        return false