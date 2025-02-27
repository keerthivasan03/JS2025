import csv
data=[["Name", "Department", "Salary"],

["Aisha Khan", "Engineering", "80000"],

["Jules Lee", "Marketing", "67000"],

["Queenie Corbit", "Human Resources", "90000"]]
file_location="C:\\Users\\keerthivasan.a\\Book_2.csv"
with open(file_location,"w") as suma:
    writing=csv.writer(suma)
    writing.writerows(data)

file_location_1="C:\\Users\\keerthivasan.a\\Book_1.csv"
with open(file_location_1,"r") as reading:
#reading=open(file_location_1)
    reads=csv.reader(reading)
    for rows in reads:
        name, role, salary =rows
        print("name:{}, role:{},salary:{}".format(name, role, salary))
file_location_2="C:\\Users\\keerthivasan.a\\Book_1.csv"
with open(file_location_2,"r") as readi:    
    reader=csv.DictReader(readi)
    for row in reader:
        print("name:{}, role:{},salary:{}".format(row["name"], row["username"], row["department"]))
file_location_3="C:\\Users\\keerthivasan.a\\Book_3.csv"
data=[{"Name":"Aisha Khan", "Department":"Engineering", "Salary":"80000"},{"Name":"Jules Lee", "Department":"Marketing", "Salary":"67000"},
      {"Name":"Queenie Corbit", "Department":"Human Resources", "Salary":"90000"}]
keys=["Name","Department","Salary"]
with open(file_location_3,"w") as data_key:
    writ=csv.DictWriter(data_key,fieldnames=keys)
    writ.writeheader()
    writ.writerows(data)
file_location_4="C:\\Users\\keerthivasan.a\\Book_4.csv"
csv.register_dialect("Dialact name",delimiter="|",quotechar='~',strict=False, skipinitialspace=False)
data = [
    ["Name", " Age", " City"],  # Extra spaces added intentionally
    ["Alice","34" " New York"],
    ["Bob", " 25", " Los Angeles"],
    ["Charlie", " 35", " San Francisco"]
]
with open(file_location_4,"w",newline="") as f:
    wri=csv.writer(f,dialect="Dialact name")
    wri.writerows(data)
with open(file_location_4,"r",newline="") as r:
    rea=csv.reader(r,dialect="Dialact name")
    for row in rea:
        print(row)
        
