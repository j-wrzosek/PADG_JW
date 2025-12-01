
employees:list = []

class Employee:
    def __init__(self, name:str, workplace:str, birth:int, photo:str):
        self.name = name
        self.workplace = workplace
        self.birth = birth
        self.photo = photo


def show_employee(employees_data: list) -> None:
   for employee in employees_data:
       print(f'Pracownik: {employee.name} pracuje w {employee.workplace}, urodził się w {employee.birth} roku.')


def add_employee(employees_data: list) -> None:
    name: str=input('Podaj imię nowego pracownika: ')
    workplace: str=input('Podaj miejsce pracy: ')
    birth: int=int(input('Podaj rok urodzenia pracownika: '))
    photo: str=input("Wprowadź link do zdjęcia: ")
    employees_data.append(Employee(name=name, workplace=workplace, birth=birth, photo=photo))

def update_employee(employees_data: list) -> None:
    tmp_name: str=input('Podaj imie pracownika do edycji: ')
    for employee in employees_data:
        if employee.name == tmp_name:
            employee.name = input('Podaj nowe imie pracownika: ')
            employee.workplace = input('Podaj nowe miejsce pracy: ')
            employee.birth = int(input('Podaj nowy rok urodzenia pracownia: '))



def remove_employee(employees_data: list) -> None:
    tmp_name: str=input('Podaj imie pracownika do usuniecia: ')
    for employee in employees_data:
        if employee.name == tmp_name:
            employees_data.remove(employee)

add_employee(employees)

print(Employee)

show_employee(employees)