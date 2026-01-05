import requests
from urllib.parse import quote
import time

employees:list = []
parks:list = []


class Park:
    def __init__(self, alias:str, address:str, category:str, logo:str, map_widget=None):
        self.alias = alias
        self.address = address
        self.category = category
        self.logo = logo
        self.coords = self.get_coords()
        self.marker = None
        if map_widget:
            self.marker = map_widget.set_marker(self.coords[0], self.coords[1], text=self.alias)

    def __str__(self):
        return f"{self.alias} - {self.address}"

    def get_coords(self):
        alias_encoded = quote(self.alias)
        url: str = f'https://nominatim.openstreetmap.org/search?q={alias_encoded},Poland&format=json&limit=1&addressdetails=1'
        headers = {
            'User-Agent': 'ParkManager/1.0 (https://github.com/j-wrzosek/PADG_JW; contact: 123456@gmail.com)',
            'Accept': 'application/json',
            'Accept-Language': 'pl,en'
        }

        time.sleep(4)

        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()

        if data and len(data) > 0:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            print(f"Znaleziono: {latitude}, {longitude}")
            return [latitude, longitude]
        return [52.0, 21.0]

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



def show_park(parks_data: list):
   return [str(park) for park in parks_data]


def add_park(parks_data: list, alias: str, address: str, category: str, logo: str, map_widget=None) -> None:
    new_park = Park(alias=alias, address=address, category=category, logo=logo, map_widget=map_widget)
    parks_data.append(new_park)


def get_park_by_alias(parks_data: list, alias:str):
    for park in parks_data:
        if park.alias == alias:
            return park
    return None

def update_park(parks_data: list, index: int, alias: str, address: str, category: str, logo: str) -> None:

        park = parks_data[index]
        park.alias = alias
        park.address = address
        park.category = category
        park.logo = logo

        park.coords = park.get_coords()
        if park.marker:
            park.marker.set_position(park.coords[0], park.coords[1])
            park.marker.set_text(text=park.alias)


def remove_park(parks_data: list, index: int) -> None:
    park = parks_data[index]
    if park.marker:
        park.marker.delete()
    parks_data.pop(index)


# if __name__ == '__main__':
#     add_employee(employees)
#     print(Employee)
#     show_employee(employees)



