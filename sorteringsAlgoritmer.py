import random, tests


def insertionSort(items):
    items = items.copy()
    for x in range(0, len(items)):
        for y in range(x, len(items)):
            if items[x] > items[y]:
                items[x], items[y] = items[y], items[x]
    return items



if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = insertionSort

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




