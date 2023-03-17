import pygame
import random
import time
#17:57 / 1:35:21
listOfChoice = []
#Pygame coding basics learned from TechWithTim
WHITE = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 1000, 500
tempRect = 0
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
second_surface = pygame.Surface([100, 200])
SCREEN.fill(WHITE)


def fillList(listOfChoice):
    for i in range(1, 101):
        listOfChoice.append(i)


fillList(listOfChoice)


def randomizeList(listOfChoice):
    return random.shuffle(listOfChoice)


randomizeList(listOfChoice)
print(listOfChoice)


def drawingOnScreen ():
    width = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(len(listOfChoice)):
        #Potential improvement could be changing listOfChoice to fractions and then multiplying them by the height
        tempRect = pygame.Surface([WIDTH/len(listOfChoice), listOfChoice[i]])
        placement = 500 - listOfChoice[i]
        SCREEN.blit(tempRect, (width, placement))
        width = width + 10
        pygame.display.update()
        pygame.event.get()


def screenControl ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
#Reminder to Self for NEXT SESSION Fix Index problem and Prevent Crashes (Potentially from miscoded sorts)
        selectionSort(listOfChoice)
        drawingOnScreen()
    pygame.quit()

#Credit to Geeks for Geeks Website for pseudocode on how to do insertion sort
def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j-1]
            j = j -1
            drawingOnScreen()

#Credit to Geeks for Geeks Website for pseudocode on how to do selection sort
def selectionSort(list):
    for i in range(0, len(list)):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[minIndex], list[i] = list[i], list[minIndex]
        drawingOnScreen()
    return list

def bubbleSort(list):
    while order(list) == False:
        for i in range(0, len(list)):
            if list[i] > list[i + 1]:
                list.insert(i, i + 1)
                list.pop(i + 2)
            time.sleep(0.5)
            drawingOnScreen()
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