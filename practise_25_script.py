#Library script to check whether we have added data in collection
import unittest
class Library:
    def __init__(self):
        self.collection=[]
    def add_book(self, add_book): #adding book to collection
        self.collection.append(add_book)
    def has_book(self, has_book):#checking that collection has that book
        return has_book in self.collection
class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        #Arrange
        book_add=Library() #calling the class to run the unittest
        new_book="Tales of narnia"
        #Act calling the program objects
        book_add.add_book(new_book)
        #Assert checkin whether the book has anything
        self.assertTrue(book_add.has_book(new_book))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
#chocolate script
class Chocolate_shop:
    def __init__(self, cake_size=str, cake_weight=int):
        self.cake_size=cake_size
        self.cake_weight=cake_weight
        self.cake_toppings=[]
        self.price=10 if self.cake_size=="round" else 8 if self.cake_size=="square" else 6
        self.price+=5 if self.cake_weight==1000 else 3 if self.cake_weight==500 else 1
    def cake_topping(self, topping=str):
        self.cake_toppings.append(topping)
        self.price+=2
    def cake_items(self):
        items=["maida","sugar", "syrup"]
        items.append("cocoa") if self.cake_weight==1000 else "Brown sugar" if self.cake_weight==500 else "White sugar"
        items+=self.cake_toppings
        return items
    def cake_price(self):
        return self.price
cake_shop=Chocolate_shop(1000,"round")
cake_shop.cake_topping("Jelly")
cake_final_items=cake_shop.cake_items()
cake_final_price=cake_shop.cake_price()
print(cake_final_items,cake_final_price)

class Test_cake_shop(unittest.TestCase):
    def testcakeprice(self):
        cake_shop=Chocolate_shop(500,"round")
        cake_final_price=cake_shop.cake_price()
        self.assertEqual(cake_final_price,7)
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test_cake_shop))
#Combination of regex and csv
log_content = """\
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (ac)
May 27 11:46:00 ubuntu.local ticky: ERROR: Timeout while retrieving information (ahmed.miller)
May 27 11:46:05 ubuntu.local ticky: INFO: Created ticket [#1235] (ahmed.miller)
May 27 11:46:10 ubuntu.local ticky: ERROR: Connection to DB failed (blossom)
May 27 11:46:15 ubuntu.local ticky: ERROR: Timeout while retrieving information (blossom)
May 27 11:46:20 ubuntu.local ticky: INFO: Created ticket [#1236] (bpacheco)
May 27 11:46:25 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (breee)
May 27 11:46:30 ubuntu.local ticky: INFO: Updated ticket [#1237] (britanni)
May 27 11:46:35 ubuntu.local ticky: ERROR: Permission denied while closing ticket (blossom)
May 27 11:46:40 ubuntu.local ticky: ERROR: The ticket was modified while updating (bpacheco)
May 27 11:46:45 ubuntu.local ticky: INFO: Updated ticket [#1238] (breee)
May 27 11:46:50 ubuntu.local ticky: ERROR: Ticket doesn't exist (flavia)
May 27 11:46:55 ubuntu.local ticky: ERROR: Timeout while retrieving information (ac)
May 27 11:47:00 ubuntu.local ticky: INFO: Created ticket [#1239] (enim.non)
May 27 11:47:05 ubuntu.local ticky: ERROR: Connection to DB failed (ahmed.miller)
May 27 11:47:10 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (ahmed.miller)
May 27 11:47:15 ubuntu.local ticky: ERROR: Permission denied while closing ticket (breee)
May 27 11:47:20 ubuntu.local ticky: ERROR: The ticket was modified while updating (enim.non)
May 27 11:47:25 ubuntu.local ticky: INFO: Updated ticket [#1240] (flavia)
May 27 11:47:30 ubuntu.local ticky: ERROR: Ticket doesn't exist (breee)
May 27 11:47:35 ubuntu.local ticky: INFO: Created ticket [#1241] (ahmed.miller)
May 27 11:47:40 ubuntu.local ticky: ERROR: Timeout while retrieving information (blossom)
May 27 11:47:45 ubuntu.local ticky: ERROR: Connection to DB failed (breee)
May 27 11:47:50 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (flavia)
May 27 11:47:55 ubuntu.local ticky: INFO: Updated ticket [#1242] (ac)
May 27 11:48:00 ubuntu.local ticky: ERROR: Timeout while retrieving information (enim.non)
May 27 11:48:05 ubuntu.local ticky: ERROR: Connection to DB failed (flavia)
May 27 11:48:10 ubuntu.local ticky: INFO: Created ticket [#1243] (enim.non)
May 27 11:48:15 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (blossom)
May 27 11:48:20 ubuntu.local ticky: ERROR: Permission denied while closing ticket (ahmed.miller)
May 27 11:48:25 ubuntu.local ticky: ERROR: The ticket was modified while updating (blossom)
May 27 11:48:30 ubuntu.local ticky: INFO: Created ticket [#1244] (flavia)
"""
filepath1="C:\\Users\\keerthivasan.a\\syslog.log"
with open(filepath1, "w") as file:
    file.write(log_content)

print("syslog.log file has been created successfully.")

import csv
import re
import operator
import os
print(os.path.exists("C:\\Users\\keerthivasan.a\\syslog.log"))
per_user={}
error={}
#using csv we are reading using forloop and check whether it is error or info and updating the count
with open("C:\\Users\\keerthivasan.a\\syslog.log","r",newline="") as extract:
    #read=csv.reader(extract)
    for line in extract:
        searching=r"ticky: (INFO|ERROR): (.+) \(([\w.]+)\)"
        capture=re.search(searching,line)
        print(capture)
        #code, error_message, user=capture[1],capture[2],capture[3]
        code, error_message, user=capture.groups()
        if error_message not in error:
            error[error_message]=1
        else:
            error[error_message]+=1
        #error[error_message] = error.get(error_message, 0) + 1
        if user not in per_user:
            per_user[user]={'INFO':0,'ERROR':0}
        if code=="INFO":
            per_user[user]["INFO"]+=1
        elif code=="ERROR":
            per_user[user]["ERROR"]+=1
    print(error,per_user)
error_list=sorted(error.items(),key=operator.itemgetter(1),reverse=True)
#per_user_list=sorted(per_user.items(),key=operator.itemgetter(1,"ERROR"),reverse=False)
per_user_list=sorted(per_user.items(),key=operator.itemgetter(0))
#write error list
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv","w",newline="") as error_write:
    error_generate=csv.writer(error_write)
    error_generate.writerow(["Error","Count"])# this value is used to read below
    #error_generate.writerow([key, value] for key,value in error_list)
    for key,value in error_list:
        error_generate.writerow([key, value])
#Read error list
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "r") as error_read:
        error_reader=csv.DictReader(error_read)
        for row in error_reader:
            print("Error:{}, Count:{} ".format(row["Error"],row["Count"]))
#write user list
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv","w",newline="") as user_write:
    user_generate=csv.writer(user_write)
    user_generate.writerow(["User","Info","Error"])
    #error_generate.writerow([key, value["INFO"],value["ERROR"]] for key,value in per_user_list)
    for key,value in per_user_list:
        user_generate.writerow([key, value["INFO"],value["ERROR"]])
#Read user list
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "r") as user_read:
    user_reader=csv.DictReader(user_read)
    for row in user_reader:
        print("User:{}, Info:{}, Error:{} ".format(row["User"],row["Info"],row["Error"]))

#updated of above script using chat gpt
import csv
import re
import operator
import os

# ✅ Check if file exists
print(os.path.exists("C:\\Users\\keerthivasan.a\\syslog.log"))

# ✅ Initialize dictionaries
per_user = {}
error = {}

# ✅ Read syslog file
with open("C:\\Users\\keerthivasan.a\\syslog.log", "r", newline="") as extract:
    for line in extract:
        # ✅ Fixed regex to capture only ERROR messages
        searching = r"ticky: (ERROR): (.+) \(([\w.]+)\)"
        capture = re.search(searching, line)

        if not capture:  # ✅ Skip if no match
            continue

        code, error_message, user = capture.groups()

        # ✅ Count errors
        error[error_message] = error.get(error_message, 0) + 1

        # ✅ Initialize user dictionary if new
        if user not in per_user:
            per_user[user] = {"INFO": 0, "ERROR": 0}

        # ✅ Increment ERROR counts
        per_user[user]["ERROR"] += 1

# ✅ Read INFO logs separately to track INFO counts correctly
with open("C:\\Users\\keerthivasan.a\\syslog.log", "r", newline="") as extract:
    for line in extract:
        searching_info = r"ticky: (INFO): .+ \(([\w.]+)\)"
        capture_info = re.search(searching_info, line)

        if capture_info:
            user = capture_info.group(1)
            if user not in per_user:
                per_user[user] = {"INFO": 0, "ERROR": 0}
            per_user[user]["INFO"] += 1  # ✅ Increment INFO count

# ✅ Sort error messages by count (descending)
error_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

# ✅ Sort user statistics by username (ascending)
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

# ✅ Write error messages CSV
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "w", newline="") as error_write:
    error_generate = csv.writer(error_write)
    error_generate.writerow(["Error", "Count"])  # ✅ Add header
    for key, value in error_list:
        error_generate.writerow([key, value])

# ✅ Read and print error messages
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "r") as error_read:
    error_reader = csv.DictReader(error_read)
    for row in error_reader:
        print("Error: {}, Count: {}".format(row["Error"].strip(), row["Count"].strip()))  # ✅ Fixed

# ✅ Write user statistics CSV
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "w", newline="") as user_write:
    user_generate = csv.writer(user_write)
    user_generate.writerow(["User", "Info", "Error"])  # ✅ Add header
    for key, value in per_user_list:
        user_generate.writerow([key, value["INFO"], value["ERROR"]])

# ✅ Read and print user statistics
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "r") as user_read:
    user_reader = csv.DictReader(user_read)
    for row in user_reader:
        print("User: {}, Info: {}, Error: {}".format(row["User"].strip(), row["Info"].strip(), row["Error"].strip()))  # ✅ Fixed

#Read file from csv
import csv
from pprint import pprint

def convert_employee_data(file_path):
    with open(file_path, "r") as dictionary:
        # Register CSV dialect with space as delimiter
        csv.register_dialect("Employee", delimiter=" ")
        convert_dic = csv.DictReader(dictionary, dialect="Employee")
        
        add_dic = []
        for data in convert_dic:
            add_dic.append(data)
        
        return add_dic

def filter_employees(employee_data, age_threshold=25):
    # Filter employees older than age_threshold
    filtered = []
    for emp in employee_data:
        if int(emp['Age']) > age_threshold:
            filtered.append(emp)
    
    return filtered

def write_filtered_data(filtered_data, output_file):
    # Write filtered data to new CSV
    if not filtered_data:
        print("No data to write.")
        return
    
    fieldnames = filtered_data[0].keys()

    with open(output_file, "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in filtered_data:
            writer.writerow(row)
    
    print(f"Filtered data written to {output_file}")

# --- Running the Code ---
file_path = "employee_data.csv"  # Replace with your input CSV file path
output_file = "filtered_employee_data.csv"

# Step 1: Read employee data
employee_data = convert_employee_data(file_path)
print("Original Employee Data:")
pprint(employee_data)

# Step 2: Filter employees (e.g., Age > 25)
filtered_employees = filter_employees(employee_data, age_threshold=25)
print("\nFiltered Employees (Age > 25):")
pprint(filtered_employees)

# Step 3: Write filtered data to a new CSV
write_filtered_data(filtered_employees, output_file)

#Not important
import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

usernames1 = {}
name1 = ["good_user","bad user"]
for x in name1:
    
    usernames1[x] = usernames1.get(x, 0) + 1
    print(usernames1)
    usernames1[x] = usernames1.get(x, 0) + 1
    print(usernames1)

usernames2 = {}
name2 = ["good_user","bad user"]
for x in name2:
    
    usernames2[x] = usernames2.get(x, 0) + 1
    usernames2[x] = usernames2.get(x, 0) + 1
print(usernames2)
#Report generation

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

#just go through it
def get_event_date(even):
  return even.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.user = machine_name
    self.machine = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

"""users = current_users(events)
print(users)

generate_report(users)

def time(get_event_time):
  return get_event_time.date

def user(get_user_list):
  get_user_list.sort(key=time)"""

#Regex testcase
import re
def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result==None:
    return name
  return "{} {}".format(result[2], result[1])
class rearrangetest(unittest.TestCase):
    def test_rearrange(self):
        tt="Lovelace, Ada"
        ex="Ada Lovelace"
        self.assertEqual(rearrange_name(tt),ex)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double(self):
        testing="Keerthi, vasan A."
        Expected="vasan A. Keerthi"
        self.assertEqual(rearrange_name(testing),Expected)
    def test_singel(Self):
        tia="Keerthi"
        expected="Keerthi"
        Self.assertEqual(rearrange_name(tia),expected)
    def test_sample(self):
        self.assertEqual("foo".upper(), "FOO")
        self.assertTrue("foo".islower())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            s.split(2)
unittest.main()

#Testcases script need to understand
import csv
import os

file_path="C:\\Users\\keerthivasan.a\\employee_data.csv"
print(os.path.exists(file_path))
def convert_employee_data(file_path):
    with open (file_path,"r") as dictionary:
        csv.register_dialect("Employee")
        convert_dic=csv.DictReader(dictionary,dialect="Employee")
        add_dic=[]
        for data in convert_dic:
            add_dic.append(data)
        return add_dic
def process(add_dic):
    department_list=[]
    for departments in add_dic:
        department_list.append(departments['Department'])
    department_data={}
    for department_count in set(department_list):
        department_data[department_count]=department_list.count(department_count)
    return department_data
def write_report(file,report_file):
    with open(report_file,"w",newline="") as write:
        writing=csv.writer(write)
        writing.writerow(["Department", "Count"])  # Write header
        for key,value in sorted(file.items()):
            writing.writerow([key, value])
data_conversion=convert_employee_data(file_path)
separate_things = process(data_conversion)
write_report(separate_things,r"C:\\Users\\keerthivasan.a\\data2.csv")
print("report generated successfully")
files="C:\\Users\\keerthivasan.a\\data2.csv"
with open (files,"r") as reader:
    rrr=csv.DictReader(reader)
    for row in rrr:
        print("Department:{}, Count:{}".format(row["Department"],row["Count"]))
#writing testcases with the program
def validate_num(given_num,len_number):
    print(len(given_num))
    assert type(given_num)==str, "username must be string"
    if len_number<1:
        raise ValueError("Min value must be atleast 1")
    if len(given_num)<len_number:
        return False
    if not given_num.isalnum():
        return False
    return True
print(validate_num("432413", 2))
class TestValidate(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_num("5354A",5),True)
    def test_valid1(self):
        self.assertEqual(validate_num("534",5),False)
    def test_invalid(self):
        self.assertEqual(validate_num("5354",1),True)
    def test_value(self):
        self.assertRaises(ValueError, validate_num,"main",-1)
unittest.main()
#User email check
import csv
#GIT check
file_name="C:\\Users\\keerthivasan.a\\user_emails.csv"
mail_dic={}
search_name=["Oleg" ,"Noel"]
def search(file_name):
    with open (file_name,"r") as cs:
        reader=csv.reader(cs)
        for row in reader:
            name=row[0].lower()
            mail_dic[name]=row[1]
    return mail_dic
def update(search_name):
    if len(search_name)<2:
        return "Error: No such record found"
    full_name=search_name[0]+" "+search_name[1]
    mail_dic=search(file_name)
    return mail_dic.get(full_name.lower(),"No name present")
def main():
    print(update(search_name))

if __name__=="__main__":
    main()
#above code with testcases

#!/usr/bin/env python3
import sys
import csv
import unittest
#argv = ["Oleg" ,"Noel"]
filename = "C:\\Users\\keerthivasan.a\\user_emails.csv"
def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0]).lower()
            email_dict[name] = row[1].lower()
    return email_dict
"""#1
def find_email(argv):
    if len(argv)<2:
        return "Error: Not enough arguments. Usage: script.py FirstName LastName"
    fullname=argv[0]+" "+argv[1]
    email_dict=populate_dictionary(filename)
    return email_dict.get(fullname.lower(),"No name present")"""
#2
def find_email(argv):
# Return an email address based on the username given
# Create the username based on the command line input.
    try:
        fullname = str(argv[0] + " " + argv[1])
    # Preprocess the data
        email_dict = populate_dictionary(filename)
    # Find and print the email
        return email_dict.get(fullname.lower(),"No email address found")
    except IndexError:
        return "Missing parameters"
"""#3
def find_email(argv):
    # Return an email address based on the username given
   # Create the username based on the command line input.
    try:
        fullname = str(argv[0] + " " + argv[1])
        # Preprocess the data
        email_dict = populate_dictionary(filename)
        # If email exists, print it
        if email_dict.get(fullname.lower()):
          return email_dict.get(fullname.lower())
        else:
          return "No email address found"
    except IndexError:
            return "Missing parameters"
"""
def main():
    print(find_email(["Oleg" ,"Noel"]))

if __name__ == "__main__":
    main()

class Testsearch(unittest.TestCase):
    def test_search(self):
        testcase=["Oleg" ,"Noel"]
        excepted="noel@abc.edu"
        self.assertEqual(find_email(testcase),excepted)
    def test_search1(self):
        testcase1=["Oleg"]
        excepted1="Missing parameters"
        self.assertEqual(find_email(testcase1),excepted1)
    def test_two_name(self):
        testcase = ["Roy","Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)
    
if __name__=="__main__":
    unittest.main()





        