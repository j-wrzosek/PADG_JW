
employees:list = [
    {'name': 'Bogdan', 'workplace': 'Ogród Saski', 'birth': 1999}


]

def add_employee(employees_data: list) -> None:
    name: str=input('Podaj imię nowego pracownika: ')
    workplace: str=input('Podaj miejsce pracy: ')
    birth: int=int(input('Podaj rok urodzenia pracownika: '))
    employees_data.append({'name': name, 'workplace': workplace, 'birth': birth})

def show_employee(employees_data: list) -> None:
   for employee in employees_data:
       print(f'Pracownik: {employee["name"]} pracuje w {employee["workplace"]}, urodził się w {employee["birth"]} roku.')

add_employee(employees)
show_employee(employees)