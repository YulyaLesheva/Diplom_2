import uuid

from data.constants import DEFAULT_PASSWORD, DEFAULT_NAME


def generate_email():
    return f"test_{uuid.uuid4()}@yandex.ru"


def generate_password():
    return DEFAULT_PASSWORD


def generate_name():
    return DEFAULT_NAME
