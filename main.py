import pygame
import random
import time
import sys
listOfChoice = []
# Pygame coding basics learned from TechWithTim
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
WIDTH, HEIGHT = 1000, 500
tempRect = 0
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
SCREEN.fill(WHITE)
sorting = False
sortingType = "Nothing"

def fillList(listOfChoice):
    for i in range(1, 101):
        listOfChoice.append(i)


fillList(listOfChoice)


def randomizeList(listOfChoice):
    return random.shuffle(listOfChoice)


randomizeList(listOfChoice)
print(listOfChoice)

#Credit to Geeks for Geeks Website for pseudocode on how to do insertion sort
def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j-1]
            j = j -1
            time.sleep(0.1)
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
        time.sleep(0.1)
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


def drawingOnScreen ():
    global sorting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    width = 0
    SCREEN.fill(WHITE)
    # Button help from GeeksforGeeks.org on how to make a button
    if not sorting:
        insertionButton = pygame.Rect([270, 150, 200, 100])
        selectionButton = pygame.Rect([520, 150, 200, 100])
        pygame.draw.rect(SCREEN, BLACK, insertionButton)
        pygame.draw.rect(SCREEN, BLACK, selectionButton)
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if insertionButton.collidepoint(mouse):
                sorting = True
                sortingType = "insertion"
    else:
        for i in range(len(listOfChoice)):
            #Potential improvement could be changing listOfChoice to fractions and then multiplying them by the height
            tempRect = pygame.Surface([WIDTH/len(listOfChoice), listOfChoice[i]])
            placement = 500 - listOfChoice[i]
            SCREEN.blit(tempRect, (width, placement))
            width = width + 10

    pygame.display.update()


def screenControl ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        selectionSort(listOfChoice)
        drawingOnScreen()
    pygame.quit()


screenControl()