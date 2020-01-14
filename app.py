from db import Database
import csv

db = Database('Business.db')

with open('vendas.csv') as csv_file:
    csv_reader =  csv.reader(csv_file,delimiter=',')
    line count = 0
    for row in csv_reader

def insertVendas(csvfile):
    with open csvfile(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        db.insert 
