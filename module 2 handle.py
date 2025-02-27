#!/usr/bin/env python3
import csv
import os
csv_file_location="C:\\Users\\keerthivasan.a\\employee_data.csv"

print(os.path.exists("C:\\Users\\keerthivasan.a\\employee_data.csv"))

#Convert employee data to dictionary
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open (csv_file_location, "r") as file_location:
        employee_file = csv.DictReader(file_location, dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
        return employee_list

#Process employee data
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

#Generate a report
def write_report(dictionary, report_file):
    #report_file="C:\\Users\\keerthivasan.a\\data.csv"
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')


employee_list = read_employees(csv_file_location)
department_summary = process_data(employee_list)
write_report(department_summary, r"C:\\Users\\keerthivasan.a\\data1.csv")

print("Report generated successfully!")
file_location_2="C:\\Users\\keerthivasan.a\\data1.csv"
with open(file_location_2,"r") as readi:    
    reader=csv.DictReader(readi)
    for row in reader:
        print("Department:{}", "count:{}".format(row["Department"],row["count"]))

"""file_location_2 = r"C:\Users\keerthivasan.a\data.csv"
with open(file_location_2, "r") as read_file:
    reader = csv.DictReader(read_file)
    for row in reader:
        print(f"Department: {row['Department']}, Count: {row['Count']}")""" 

