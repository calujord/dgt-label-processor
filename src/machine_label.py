import re

import requests
from bs4 import BeautifulSoup

import constants
from exceptions.request_exception import RequestException
from src.label import DgtLabel


class DgtMachine:
    plate: str

    def __init__(self, plate: str):
        """
        Init machine.

        @:param plate
        """
        self.plate = plate.replace('-', '').strip()
        self.dgt_url = f"{constants.DGT_URL}/es/vehiculos/informacion-de-vehiculos/distintivo-ambiental/index.html?matricula="

    def __str__(self) -> str:
        return self.plate

    def process_label(self) -> DgtLabel:
        """Get Label of DGT"""
        data_result = requests.get(f'{self.dgt_url}{self.plate}')

        if data_result.status_code != 200:
            raise RequestException("Error in request")
        else:
            # process data form html response
            response = data_result.text
            # transformation soup
            soup = BeautifulSoup(response, 'html.parser')
            # Example: find a specific element
            div_element = soup.find('div', class_="border rounded border-success mb-3")  # Adjust the selector as needed

            if div_element and div_element.find('img'):
                if div_element.find('img')['src'] is None:
                    raise RequestException("Not found image")

                url_label = constants.DGT_URL + div_element.find('img')['src']

                match = re.search(r'_(\w)_sin_fondo\.svg', url_label)
                if match:
                    return DgtLabel(
                        url_image=constants.DGT_URL + div_element.find('img')['src'],
                        value=match.group(1)
                    )

            raise RequestException("Not found label")
