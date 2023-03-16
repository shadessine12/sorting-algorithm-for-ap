import pygame
import random
#17:57 / 1:35:21
listOfChoice = []
#Pygame coding basics learned from TechWithTim
WHITE = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 900, 500

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

def drawingOnScreen ():

    pygame.display.update()

def screenControl ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawingOnScreen()
    pygame.quit()


def fillList():
    for i in (1, 101):
        listOfChoice.append(i)

def randomizeList():
    return random.shuffle(listOfChoice)

#Credit to Geeks for Geeks Website for pseudocode on how to do insertion sort
def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j-1]
            j = j -1

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
    while order(list) == False:
        for i in range(0, len(list)):
            if list[i] > list[i + 1]:
                list.insert(i, i + 1)
                list.pop(i + 2)
    return list

def order(list):
    truthCounter = 0
    for i in range(0, len(list)):
        if list[i] > list[i - 1] and list[i] < list[i + 1]:
            truthCounter = truthCounter + 1
    if truthCounter == len(list):
        return True 
    else:
        return False

screenControl()