from ParkManager_lib.model import Employee, Park, User

employees:list = []
parks:list = []
users:list = []


def show_user(users_data: list):
    return [str(user) for user in users_data]


def add_user(users_data: list, username: str, location: str, user_type: str, fav_park: str):

    new_user = User(username=username,location=location,user_type=user_type,fav_park=fav_park)
    users_data.append(new_user)



def get_user_by_username(users_data: list, username: str):
    for user in users_data:
        if user.username == username:
            return user
    return None


def update_user(users_data: list, index: int, username: str, location: str, user_type: str, fav_park: str):
    user = users_data[index]
    user.username = username
    user.location = location
    user.user_type = user_type
    user.fav_park = fav_park
    user.coords = user.get_coords()


def remove_user(users_data: list, index: int):
    users_data.pop(index)


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






