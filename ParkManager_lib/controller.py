
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

def update_employee(employees_data: list) -> None:
    tmp_name: str=input('Podaj imie pracownika do edycji: ')
    for employee in employees_data:
        if employee['name'] == tmp_name:
            employee['name'] = input('Podaj nowe imie pracownika: ')
            employee['workplace'] = input('Podaj nowe miejsce pracy: ')
            employee['birth'] = input('Podaj nowy rok urodzenia pracownia: ')


def remove_employee(employees_data: list) -> None:
    tmp_name: str=input('Podaj imie pracownika do usuniecia: ')
    for employee in employees_data:
        if employee['name'] == tmp_name:
            employees_data.remove(employee)


add_employee(employees)
update_employee(employees)
add_employee(employees)
remove_employee(employees)
show_employee(employees)
