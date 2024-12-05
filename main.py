import csv, random
from faker import Faker

print("made by starlover")

fake = Faker()

def generate_csv():
    file_path = 'user.csv'
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Firstname', 'Lastname', 'Password', 'Birthday', 'Username']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print("\nGenerated User Data:")
        print("-" * 80)
        for i in range(20):
            firstname = fake.first_name()
            lastname = fake.last_name()
            password = fake.password()
            birthday = fake.date_of_birth().strftime('%m/%d/%Y')
            username = f"{fake.first_name().lower()}{fake.last_name().lower()}{random.randint(1, 100)}@{fake.domain_name()}"
            data = {
                'Firstname': firstname,
                'Lastname': lastname,
                'Password': password,
                'Birthday': birthday,
                'Username': username
            }
            writer.writerow(data)
            print(f"User {i+1}:")
            for key, value in data.items():
                print(f"{key}: {value}")
            print("-" * 80)

generate_csv()