from ispit import get_ispit
from utilities import unos_intervala
from .redovni_student import RedovniStudent
from .vanredni_studentć import VanredniStudent
from .student import Student

def unos_studenta(ispiti, redni_broj):
    print('Odaberite tip studenta: ')
    print('\t1.rednovni student')
    print('\t2.vanredni student')
    tip_studenta = int(input('Unesite tip studenta: '))


    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    print('Za odabir ispita')
    odabrani_ispit = unos_intervala(1, len(ispiti))
    ispit = ispiti[odabrani_ispit - 1]

    if tip_studenta == 1:
        broj_prijava = int(input('Unesite broj priojava: '))
        return  RedovniStudent(ime, prezime, ispit, broj_prijava)

    elif tip_studenta == 2:
        return VanredniStudent(ime, prezime, ispit)

    return Student(ime, prezime, ispit)




