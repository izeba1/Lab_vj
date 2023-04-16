from ispit import get_ispit

def unos_studenta(ispiti, redni_broj):
    student = {}
    student['ime'] = input(f"Unesite ime {redni_broj}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i in enumerate(ispiti, start=1):
        print(get_ispit(ispiti, i))



    return student



