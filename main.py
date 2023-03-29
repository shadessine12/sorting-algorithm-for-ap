# Make sure to credit for help with button
# Creating all global variables and importing necessary libraries for program to run.
import pygame
import random
import time
import sys
pygame.init()
listOfChoice = []
# Pygame coding basics learned from TechWithTim pygame tutorial video
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
'''
Creating the randomized list with the help of two functions, fillList and randomizeList.
fillList is used to add all of the elements to the list which is called listOfChoice.
randomizeList is using a function given to every Python user 
which will randomize the indexes of the list in question.
'''
def fillList(listOfChoice):
    for i in range(1, 101):
        listOfChoice.append(i)


fillList(listOfChoice)


def randomizeList(listOfChoice):
    return random.shuffle(listOfChoice)


randomizeList(listOfChoice)
print(listOfChoice)

#Credit to Geeks for Geeks Website for pseudocode on how to do insertion sort
'''
A kind of sort that keeps swapping the number until it is at its lowest point.
It will keep doing this to each number in the list until everything is set up.
'''
def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j-1]
            j = j -1
            time.sleep(0.1)
            drawingOnScreen()

#Credit to Geeks for Geeks Website for pseudocode on how to do selection sort
'''
A kind of sort that finds the lowest number in the list and switches it to the current lowest position.
It will only take one run through all of the list's values for everything to be sorted.
'''
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


'''
This function is used as the function 
that will create the screen that shall show the sorting of the list through rectangles. 
This function first shows a menu screen where the type of sort can be selected.
Once the type of sort is selected, it shall begin sorting itself through the screenControl function 
which shall start to run it.
'''
def drawingOnScreen ():
    global sorting
    global sortingType
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    width = 0
    SCREEN.fill(WHITE)
    # Button creation help from GeeksforGeeks.org on how to make a button
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


'''
This function is used as a main way of running all of the smaller functions together. 
This function helps determine what kind sort shall be used from the data outputted by the drawScreen function.
It will then use the drawingScreen function to implement this method.
'''
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