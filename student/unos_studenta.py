from ispit import get_ispit
from utilities import unos_intervala

def unos_studenta(ispiti, redni_broj):
    student = {}
    student['ime'] = input(f"Unesite ime {redni_broj}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i in enumerate(ispiti, start=1):
        print(get_ispit(ispiti, i))

    x = len(ispiti)
    odabrani_ispit = unos_intervala(1, x)
    student['ispit'] = ispiti[odabrani_ispit - 1]
    return student

    return student



