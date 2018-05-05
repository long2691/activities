import os
import csv

csvpath = os.path.join(".", "employees.csv")

new_employee_data = []
#read data into a dictionary and create an email
with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:  
        first_name = row["First Name"]
        last_name = row["Last Name"]
        email = first_name +  "," + last_name + "@example.com"
        #email = f"{first_name}-{last_name}@example.com"
        #print(email)
        new_employee_data.append({
            "First Name": first_name,
            "Last Name": last_name,
            "SSN": row["SSN"],
            "email": email
        })
print(new_employee_data)
# grab the filename from originalpath
print(csvpath)
_ , filename = os.path.split(csvpath)
print(_)
print(filename)

csv2path = os.path.join(".","output", filename)
with open(csv2path, "w") as csvfile:
    fieldnames = ["Last Name", "First Name", "SSN","email"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for dog in new_employee_data:
        writer.writerow(dog)