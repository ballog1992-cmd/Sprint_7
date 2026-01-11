import requests
import random
import string


def register_new_courier_and_return_login_password():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
        }

def non_existent_courier_body():
    return {
        "login": "Uchiha",
        "password": "Haringan",
        "firstName": "Saske"
    }