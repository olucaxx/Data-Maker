import csv

from column_types.name import Name
from column_types.age import Age
from column_types.phone_number import PhoneNumber
from column_types.cpf import CPF


def generate_random_data(amount):
    data = []
    for _ in range(amount):
        data.append([Name(), Age(), PhoneNumber(), CPF()])
        
    return data

data = generate_random_data(100)

CSV_FILE = "random_data.csv"

with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["name", "age", "phone_number", "cpf"])
    
    writer.writerows(data)
    
print("arquivo gerado com sucesso slkk")