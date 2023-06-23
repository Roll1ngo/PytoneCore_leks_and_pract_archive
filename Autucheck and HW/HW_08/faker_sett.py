from datetime import datetime, timedelta
from collections import defaultdict
from faker import Faker
from faker.providers import person
from rich import print


fake = Faker("uk-UA")
fake.add_provider(person)
Faker.seed(1)

employes = list()


for i in range(30):
   
    fake_persons = dict()
    fake_persons["name"] = fake.name()
    fake_persons["birthday"] =fake.profile()["birthdate"]
    employes.append(fake_persons)
        
print(employes)









