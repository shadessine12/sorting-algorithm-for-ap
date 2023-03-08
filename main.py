def bubbleSort(list):
    while order(list) == false:
        for i in range(0, list.length):
            if list[i] > list[i + 1]:
                list.insert(i, i + 1)
                list.pop(i + 2)
    return list


def order(list):
    truthCounter = 0
    for i in range(0, list.length):
        if list[i] > list[i - 1] && list[i] < list[i + 1]:
            truthCounter = truthCounter + 1
    if truthCounter == list.length:
        return true 
    else:
        return false