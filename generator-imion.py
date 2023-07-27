import csv
import random

class NotSex (Exception):
    pass

try:
    sex = str(input('Podaj swoją płeć (M/K): '))
    if sex in ['m', 'M', 'k', 'K']:
        print("Poprawna wartość.")
    else:
        raise NotSex
except NotSex:
    print('Niepoprawna wartość.')