from ispit import ispis_ispita

def ispis_studenta(student):
    print(f"\tStudent {student['ime']} {student['prezime']} je prijavio:")
    ispis_ispita(student['ispit'])
