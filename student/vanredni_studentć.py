from .student import Student
from .izracunskolarine import IzracunSkolarine

class VanredniStudent(Student, IzracunSkolarine):
    def __init__(self, ime, prezime, ispit):
        super().__init__(ime, prezime, ispit)

    def ispis(self):
        print(f'Vanredni student {self.ime} {self.prezime} prijavio je ispit: ')
        self.ispit.ispis()
        print(f'\tPotrebno je uplatiti  {self.izracun_skolarine()} eura')

    def izracun_skolarine(self):
        return self.ispit.kolegij.ECTS * 50