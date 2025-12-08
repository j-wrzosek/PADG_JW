import requests
from urllib.parse import quote
import time

employees:list = []

class Employee:
    def __init__(self, name:str, workplace:str, birth:int, photo:str, map_widget=None):
        self.name = name
        self.workplace = workplace
        self.birth = birth
        self.photo = photo
        self.coords = self.get_coords()
        self.marker = None
        if map_widget:
            self.marker = map_widget.set_marker(self.coords[0], self.coords[1], text=self.name)


    def __str__(self):
        return f"{self.name} - {self.workplace}"


    def get_coords(self):
        workplace_encoded = quote(self.workplace)
        url: str = f'https://nominatim.openstreetmap.org/search?q={workplace_encoded},Poland&format=json&limit=1&addressdetails=1'
        headers = {
            'User-Agent': 'ParkManager/1.0 (https://github.com/j-wrzosek/PADG_JW; contact: 123456@gmail.com)',
            'Accept': 'application/json',
            'Accept-Language': 'pl,en'
        }

        time.sleep(4)
        print(f"Szuka współrzędnych dla: {self.workplace}")
        print(f"URL: {url}")
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Status code: {response.status_code}")
        print(f"Response text (first 200 chars): {response.text[:200]}")
        data = response.json()

        if data and len(data) > 0:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            print(f"Znaleziono: {latitude}, {longitude}")
            return [latitude, longitude]
        return [52.0 , 21.0]


def show_employee(employees_data: list):
   return [str(employee) for employee in employees_data]


def add_employee(employees_data: list, name: str, workplace: str, birth: int, photo: str, map_widget=None) -> None:

        new_employee = Employee(name=name, workplace=workplace, birth=birth, photo=photo, map_widget=map_widget)
        employees_data.append(new_employee)

def get_employee_by_name(employees_data: list, name:str):
    for employee in employees_data:
        if employee.name == name:
            return employee
    return None


def update_employee(employees_data: list, index: int, name: str, workplace: str, birth: int, photo: str) -> None:

        employee = employees_data[index]
        employee.name = name
        employee.workplace = workplace
        employee.birth = birth
        employee.photo = photo

        employee.coords = employee.get_coords()
        if employee.marker:
            employee.marker.set_position(employee.coords[0], employee.coords[1])
            employee.marker.set_text(text=employee.name)


def remove_employee(employees_data: list, index: int) -> None:

        employee = employees_data[index]
        if employee.marker:
            employee.marker.delete()
        employees_data.pop(index)


# if __name__ == '__main__':
#     add_employee(employees)
#     print(Employee)
#     show_employee(employees)



