import pygame
import random
import time
import sys
pygame.init()
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
smallFont = pygame.font.SysFont('Corbel', 35)
textIS = smallFont.render('Insertion Sort', True, WHITE)
textSS = smallFont.render('Selection Sort', True, WHITE)

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


def drawingOnScreen ():
    global sorting
    global sortingType
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
        SCREEN.blit(textIS, (275, 185))
        SCREEN.blit(textSS, (525, 185))
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if insertionButton.collidepoint(mouse):
                sorting = True
                sortingType = "insertion"
            if selectionButton.collidepoint(mouse):
                sorting =True
                sortingType = "selection"
    else:
        for i in range(len(listOfChoice)):
            #Potential improvement could be changing listOfChoice to fractions and then multiplying them by the height
            tempRect = pygame.Surface([WIDTH/len(listOfChoice), listOfChoice[i]])
            placement = 500 - listOfChoice[i]
            SCREEN.blit(tempRect, (width, placement))
            width = width + 10

    pygame.display.update()

'''Function is used to run all '''
def screenControl ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if sortingType == "insertion":
            insertionSort(listOfChoice)
            drawingOnScreen()
        elif sortingType == "selection":
            selectionSort(listOfChoice)
            drawingOnScreen()
        drawingOnScreen()
    pygame.quit()


screenControl()