from faker import Faker
from faker.providers import person, profile, phone_number
from rich import print
from rich.table import Table


dct = {i: i**3 for i in range(10, 20)}

table = Table(title=" numbers")
table.add_column("number")
table.add_column("cube")

for key, value in dct.items():
    table.add_row(str(key))
