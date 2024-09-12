import random, tests
""""

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
        IndexOfMin = x #Laver en variabel for den mindste værdi og sætter lig med x
        for y in range(x, len(items)): #Opretter en løkke fra x til listens længde
            if items[IndexOfMin] > items[y]: #Tjekker om den mindste værdi fundet er større end y
                IndexOfMin = y #Hvis y er mindre end den mindste værdi bliver det den nye mindste
        items[x], items[IndexOfMin] = items[IndexOfMin], items[x] #Sætter den mindste værdi på x's plads
    return items #Returnere den rettede liste


def bubbleSort(items): #Definere den nye algoritme
    items = items.copy() #Kopiere den randomiseret liste
    for x in range(0,len(items)): # Den løkker der gøre listen mindre
        for y in range(1,len(items)-x): #den løkke der bytter
            if items[y] < items[y-1]: #hvis den tal lige før er større
                items[y-1],items[y] = items[y],items[y-1] #byt plads


    return items

def mergeSort(items): #Definere den nye algoritme
    items = items.copy() #Kopiere listen
    if len(items) > 1: #Tjekker om listen
        halvListe = len(items)//2 #Halv
        liste1 = items[:halvListe]
        liste2 = items[halvListe:]

        liste1 = mergeSort(liste1)
        liste2 = mergeSort(liste2)

        i = j = k = 0

        while i < len(liste1) and j < len(liste2):
            if liste1[i] < liste2[j]:
                items[k] = liste1.pop(i)
            else:
                items[k] = liste2.pop(j)
            k += 1

        while i < len(liste1):
            items[k] = liste1.pop(i)
            k += 1

        while j < len(liste2):
            items[k] = liste2.pop(j)
            k += 1

    return items
"""






















def combSort(items):
    items = items.copy()
    gap = len(items)
    shrink = 1.3
    Sorted = False
    while Sorted == False:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            Sorted = True
        elif gap == 9 or gap == 10:
            gap = 11

        i = 0
        while i + gap < len(items):
            if items[i] > items[i + gap]:
                items[i],items[i + gap] = items[i + gap],items[i]
                Sorted = False
            i += 1
    return items


if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = combSort

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