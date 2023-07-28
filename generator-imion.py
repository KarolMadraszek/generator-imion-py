import csv
import random

male_names = []
female_names = []

with open('Popular_Baby_Names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Gender']=='MALE':
            male_names.append(row["Child's First Name"])
        elif row['Gender']=='FEMALE':
            female_names.append(row["Child's First Name"])
class NotSex (Exception):
    pass

try:
    sex = str(input('Podaj swoją płeć (M/K): '))
    if sex in ['m', 'M']:
        random_male_name = random.choice(male_names)
        print("Wylosowane imię to:", random_male_name)
    else:
        random_female_name = random.choice(female_names)
        print("Wylosowane imię dla płci żeńskiej:", random_female_name)
except NotSex:
    print('Niepoprawna wartość.')