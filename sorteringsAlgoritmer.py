import random, tests


def badSelectionSort(items): #Definere ny algoritme
    items = items.copy() #Laver en kopi af listen
    for x in range(0, len(items)): #Opretter en løkke fra 0 til listens længde
        for y in range(x, len(items)): #Opretter en løkke fra x til listens længde
            if items[x] > items[y]:  #Tjekker om den x er større end y
                items[x], items[y] = items[y], items[x] #Bytter x og y plads
    return items

def SelectionSort(items): #Definere ny algoritme
    items = items.copy() #Laver en kopi af listen
    for x in range(0, len(items)): #Opretter en løkke fra 0 til listens længde
        IndexOfMin = items[x] #Laver en variabel for den mindste værdi og sætter lig med x
        for y in range(x, len(items)): #Opretter en løkke fra x til listens længde
            if items[IndexOfMin] > items[y]: #Tjekker om den mindste værdi fundet er større end y
                IndexOfMin = y #Hvis y er mindre end den mindste værdi bliver det den nye mindste
        items[x], items[IndexOfMin] = items[IndexOfMin], items[x] #Sætter den mindste værdi på x's plads
    return items #Returnere den rettede liste


def bubbleSort(items): #Definere den nye algoritme
    items = items.copy() #Kopiere den randomiseret liste
    for x in range(0,len(items)): # den løkker der gøre listen mindre
        for y in range(1,len(items)-x): #den løkke der bytter
            if items[y] < items[y-1]: #hvis den tal lige før er større
                items[y-1],items[y] = items[y],items[y-1] #byt plads


    return items


if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = SelectionSort

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