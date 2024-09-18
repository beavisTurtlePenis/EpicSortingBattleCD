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
        halvListe = len(items)//2 #Opretter en variabel af halvdelen af listen
        liste1 = items[:halvListe] #Opdeler liste i to dele
        liste2 = items[halvListe:]

        liste1 = mergeSort(liste1) #Bruger mergesort på begge lister
        liste2 = mergeSort(liste2)

        k = 0 #opretter en variabel som holder styr på index af den sorterede liste

        while 0 < len(liste1) and 0 < len(liste2): #Laver en løkke som tjekker om der stadig er elementer i listerne
            if liste1[0] < liste2[0]: #Tjekker om elementet i liste1 er mindre end i liste2
                items[k] = liste1.pop(0) #Indsætter elementet fra liste1 hvis det er mindst
            else:
                items[k] = liste2.pop(0) #Indsætter elementet fra liste2 hvis det er mindst
            k += 1 #Går videre til næste index i den sorterede liste

        while 0 < len(liste1): #Laver en løkke som kører når der stadig er elementer i liste1
            items[k] = liste1.pop(0) #Lægger elementet til den sorterede liste
            k += 1 #Går videre til næste index i den sorterede liste

        while 0 < len(liste2): #Laver en løkke som kører når der stadig er elementer i liste2
            items[k] = liste2.pop(0) #Lægger elementet til den sorterede liste
            k += 1 #Går videre til næste index i den sorterede liste

    return items #Returnere den sorterede liste


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
    algorithm = mergeSort

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