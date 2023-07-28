import csv
import random

with open('Popular_Baby_Names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# class NotSex (Exception):
#     pass

# try:
#     sex = str(input('Podaj swoją płeć (M/K): '))
#     if sex in ['m', 'M', 'k', 'K']:
#         print("Poprawna wartość.")
#     else:
#         raise NotSex
# except NotSex:
#     print('Niepoprawna wartość.')