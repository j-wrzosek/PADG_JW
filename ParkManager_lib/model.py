import requests
from urllib.parse import quote
import time
import random


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

        base_lat, base_lon = self.get_coords()
        self.offset_lat = random.uniform(-0.003, 0.003)
        self.offset_lon = random.uniform(-0.003, 0.003)

        self.coords = [base_lat + self.offset_lat, base_lon + self.offset_lon]


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
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()

        if data and len(data) > 0:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            print(f"Znaleziono: {latitude}, {longitude}")
            return [latitude, longitude]
        return [52.0 , 21.0]
