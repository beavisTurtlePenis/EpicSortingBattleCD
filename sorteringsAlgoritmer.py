import random, tests


def badSelectionSort(items):
    items = items.copy()
    for x in range(0, len(items)):
        for y in range(x, len(items)):
            if items[x] > items[y]:
                items[x], items[y] = items[y], items[x]
    return items


def bubbleSort(items): #Definere den nye algoritme
    items = items.copy() #copiere den randomiseret liste
    for x in range(0,len(items)): # den løkker der gøre listen mindre
        for y in range(1,len(items)-x): #den løkke der bytter
            if items[y] < items[y-1]: #hvis den tal lige før er større
                items[y-1],items[y] = items[y],items[y-1] #byt plads


    return items


if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = gnomeSort

    passedTest = True
    for i in range(10):
        l = list(range(0, 10))
        lb = l.copy()
        random.shuffle(lb)
        ls = lb.copy()
        if not tests.sortsCorrectly(ls, algorithm):
            passedTest = False
            break

    if passedTest:
        print('Succes! Algoritmen sorterer korrekt.')
    else:
        print('Fejl! Algoritmen kan ikke sortere.')

    print('blandet: ', lb)
    print('sorteret:', algorithm(ls))