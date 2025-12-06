
employees:list = []

class Employee:
    def __init__(self, name:str, workplace:str, birth:int, photo:str):
        self.name = name
        self.workplace = workplace
        self.birth = birth
        self.photo = photo

    def __str__(self):
        return f"{self.name} - {self.workplace}"

def show_employee(employees_data: list) -> list:
   return [str(employee) for employee in employees_data]


def add_employee(employees_data: list, name: str, workplace: str, birth: int, photo: str) -> bool:
    try:
        new_employee = Employee(name=name, workplace=workplace, birth=birth, photo=photo)
        employees_data.append(new_employee)
        return True
    except Exception as e:
        print(f"Błąd podczas dodawania ogrodnika: {e}")
        return False

def get_employee_by_name(employees_data: list, name:str) -> Employee:
    for employee in employees_data:
        if employee.name == name:
            return employee
    return None

def update_employee(employees_data: list, old_name: str, name: str, workplace: str, birth: int, photo: str) -> bool:
    try:
        for employee in employees_data:
            if employee.name == old_name:
                employee.name = name
                employee.workplace = workplace
                employee.birth = birth
                employee.photo = photo
                return True
        return False
    except Exception as e:
        print(f"Błąd podczas aktualizacji ogrodnika: {e}")
        return False


def remove_employee(employees_data: list, name:str) -> bool:
    try:
        for employee in employees_data:
            if employee.name == name:
                employees_data.remove(employee)
                return True
        return False
    except Exception as e:
        print(f"Błąd podczas usuwania pracownika: {e}")
        return False

# if __name__ == '__main__':
#     add_employee(employees)
#     print(Employee)
#     show_employee(employees)



