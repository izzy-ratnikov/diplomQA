import logging
import allure
import requests
from data.urls import DOMEN_API


class BaseServices:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    @allure.step('GET: {path}')
    def get(self, path, headers):  # noqa C901
        response = requests.get(DOMEN_API + path, headers=headers)
        if response.status_code == 200:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return response.json()
        elif response.status_code == 404:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False

    @allure.step('POST: {path}')
    def post(self, path, headers, body, code):  # noqa C901
        response = requests.post(DOMEN_API + path, headers=headers, data=body)
        if response.status_code == code:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False

    @allure.step('PUT: {path}')
    def put(self, path, headers, body, code):  # noqa C901
        response = requests.put(DOMEN_API + path, headers=headers, data=body)
        if response.status_code == code:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False

    @allure.step('DELETE: {path}')
    def delete(self, path, headers):  # noqa C901
        response = requests.delete(DOMEN_API + path, headers=headers)
        if response.status_code == 200:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return response.json()
        elif response.status_code == 404:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False

    @allure.step('PATCH: {path}')
    def patch(self, path, headers, code):  # noqa C901
        response = requests.patch(DOMEN_API + path, headers=headers)
        if response.status_code == code:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False

    @allure.step('UPLOAD')
    def upload(self, path, headers, file, code):  # noqa C901
        response = requests.post(DOMEN_API + path, headers=headers, files=file)
        if response.status_code == code:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'Response: {response.status_code}, {response.text}')
            return False
