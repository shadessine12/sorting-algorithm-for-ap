def bubbleSort(list):
    while order(list) == false:


def order(list):
    truthCounter = 0
    for i in range(0, list.length):
        if list[i] > list[i - 1] && list[i] < list[i + 1]:
            truthCounter = truthCounter + 1
    if truthCounter == list.length:
        return true 
    else:
        return false