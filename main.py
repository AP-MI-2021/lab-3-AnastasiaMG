def toate_elem_arithmetic_progression(l1: list[int]) -> list[int]:
    '''
    Determina daca numerele dintr un sir sunt in progresie aritmetica
    :param l1: lista de numere intregi
    :return: True daca sunt in progresie aritmetica si False in caz contrar
    '''
    r = l1[1] - l1[0]
    for i in range(1, len(l1)):
        if r != l1[i] - l1[i-1]:
            return False
    return True

def test_toate_elem_arithmetic_progression():
    assert toate_elem_arithmetic_progression([2, 4, 6, 8, 10]) is True
    assert toate_elem_arithmetic_progression([2, 3, 4, 6, 8, 10]) is False

def get_longest_arithmetic_progression(l: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu numere in p.a.
    :param l: lista de nr intregi
    :return: cea mai lunga subsecventa cu numere in p.a.
    '''
    longest_arithmetic_progression = []

    for i in range(1, len(l)):
        for j in range(i, len(l)):
            l1 = []
            l1 = l[i:j+1]
            if toate_elem_arithmetic_progression(l1) and len(l1) > len(longest_arithmetic_progression):
                longest_arithmetic_progression = l[i:j+1]
            for q in range(0, len(l1)):
                del(l1[q])
    return longest_arithmetic_progression

def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1, 2, 3, 5, 7, 9, 10]) == [3, 5, 7, 9]

def toate_elem_Div_k(l: list[int], k: int) -> list[int]:
    '''
    determina daca toate nr. dintr-o lista sunt divizibile cu k
    :param l: lista de nr. intregi
    :return : True, daca toate nr. din l sunt divizibile cu k sau False, in caz contrar
    '''
    for x in l:
        if x % k != 0:
            return False
    return True

def test_toate_elem_Div_k():
    assert toate_elem_Div_k([3, 6, 9, 3], 2) is False
    assert toate_elem_Div_k([4, 8, 24, 2], 2) is True
    assert toate_elem_Div_k([2, 3, 6, 3], 4) is False


def get_longest_div_k(l: list[int], k: int) -> list[int]:
    '''
    determina cea mai lunga subsecventa de nr. divizibile cu k
    :param 1: lista nr intregi
    :param 2: k nr la care elem se v
    :return: Cea mai lunga subsecventa cu nr div cu k
    '''
    longest_div_k = []
    for i in range(1, len(l)):
        for j in range(i, len(l)):
            if toate_elem_Div_k(l[i:j + 1], k) and len(l[i:j + 1]) > len(longest_div_k):
                longest_div_k = l[i:j + 1]
    return longest_div_k


def test_get_longest_div_k():
    assert get_longest_div_k([1, 4, 6, 14, 16, 19, 31], 2) == [4, 6, 14, 16]
    assert get_longest_div_k([1,2,3,4,6,8,9,10,12], 2) == [4, 6, 8]

def printMenu():
    print("1. Citire lista")
    print("2. Verificare fct care determina daca numerele dintr un subsir sunt div cu k")
    print("3. Afisare cea mai lunga subsecventa de nr. divizibile cu k ")
    print("4. Verificare fct care determina daca numerele dintr un subsir sunt in p.a")
    print("5. Afisare cea mai lunga subsecventa cu elem in p.a.")
    print("6. Afisare lista")
    print("7. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    test_get_longest_div_k()
    test_toate_elem_Div_k()
    test_toate_elem_arithmetic_progression()
    #test_get_longest_arithmetic_progression()

    l = []
    while True:
        printMenu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            l=citireLista()
        elif optiune == "2":
            k = int(input("Dati nr k: "))
            print(toate_elem_Div_k(l, k))
        elif optiune == "3":
            k = int(input("Dati nr k: "))
            print(get_longest_div_k(l, k))
        elif optiune == "4":
            print(toate_elem_arithmetic_progression(l))
        elif optiune == "5":
            print(get_longest_arithmetic_progression(l))
        elif optiune == "6":
            print(l)
        elif optiune == "7":
            break
        else:
            print("Optiune gresita")

main()