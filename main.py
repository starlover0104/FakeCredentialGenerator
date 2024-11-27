import csv
import os
from faker import Faker
from datetime import datetime, timedelta
import random

print("made by starlover")

fake = Faker()

def generate_csv():
    file_path = 'user.csv'
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Firstname', 'Lastname', 'Password', 'Birthday', 'Username']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(20):
            firstname = fake.first_name()
            lastname = fake.last_name()
            password = fake.password()
            birthday = fake.date_of_birth().strftime('%m/%d/%Y')
            username = f"{fake.first_name().lower()}{fake.last_name().lower()}{random.randint(1, 100)}@{fake.domain_name()}"
            writer.writerow({
                'Firstname': firstname,
                'Lastname': lastname,
                'Password': password,
                'Birthday': birthday,
                'Username': username
            })

generate_csv()