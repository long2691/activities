##cereal bonus read through the csv of cereals --- find all cereals with 5 grams of fiber or more --- fiber is column h, print those out to your terminal

import os
import csv

csvpath = os.path.join('.', "resource", "cereal.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    for row in csvreader:
        if(float(row[7]) >= 5):
            print(row)
                