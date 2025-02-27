"""import csv
file_path="C:\\Users\\keerthivasan.a\\user_emails_1.csv"
csv.register_dialect("Dialact",delimiter=",",skipinitialspace=True,strict=True)
data=[{"Name":"Harishwadha","Email":"hhh@cbre.com"}]
datas=["Name","Email"]
with open (file_path,"a",newline="") as write:
    wrote=csv.DictWriter(write,dialect="Dialact",fieldnames=datas)
    write.seek(0)
    if write.tell()==0:
        wrote.writeheader()
    wrote.writerows(data)
with open(file_path,"r",newline="") as read:
    #reader=csv.reader(read)
    #for reads in reader:
        #Name,Email=reads
       # print ("Name:{}, Email:{}".format(Name,Email))
    reader=csv.DictReader(read)
    for reads in reader:
        print("Name:{},Email:{}".format(reads["Name"],reads["Email"]))
csv.register_dialect("Dileama", delimiter=",")
data_k=["kiran","Kiran@cbre.com"],["BiaBia","Bia@gmail.com"]
with open (file_path,"a",newline="") as www:
    wwww=csv.writer(www)
    wwww.writerows(data_k)"""
"""
import re
log="July 31 07:51:48 mycomputer bad_process[123455354]: ERROR Performing package upgrade"
reg=r"\[(\d+)\]"
finl=re.search(reg,log)
print(finl[1])

print(re.search(r"[a-zA-z]*","Kiamia"))
print(re.search(r"ke.*thi","keerthi"))
print(re.search(r".com","welcome"))
print(re.search(r"\.com","new.com"))
print(re.search(r"[A-Za-z].*9","Podadai9"))
def check_sentence(loss):
    comment=r"^[A-Z][a-zA-Z\s].*[.!?]$"
    finals=re.search(comment,loss)
    return finals !=None
print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
def rearrange_name(name):
    re_write=r"(^[A-Z][a-z].*), ([A-Z][a-z\s].*[.!?]$)"
    final_update=re.search(re_write,name)
    print(final_update[2], final_update[1])
rearrange_name("Hopper, Grace M.")
def add_number(number):
    code=r"(\d{3}-\d{3}|\d{7}-\d{3})"
    kk=re.sub(code,r"+1-\1",number)
    return kk
print(add_number("Eli Jonse,684-3478675,IT specialist"))#output:Eli Jonse,+1-684-3478675,IT specialist
print(add_number("Eli Jonse,684-347-8675,IT specialist"))#output:Eli Jonse,+1-684-347-8675,IT specialist
def multi(words):
    rega=r"\b\w*[aeiouAEIOU]{3}\w*\b"
    last=re.findall(rega,words)
    return last
print(multi("Life is beauatiful"))
print(multi("Obviously, Queen is Courageous and gracious."))
print(multi("The Rambunctious, childern had to sit quietly to enjoy their delicious fooeds"))
print(multi("The order of data queuee"))
print(multi("Hello world"))

def code_regex(words):
    first_regex=re.findall(r"\b\w*\b",words)
    result=[]
    for second_regex in first_regex:
        vowels=re.findall(r"[AEIOUaeiou]",second_regex)
        if len(vowels)>=3:
            result.append(second_regex)    
    return result
print(code_regex("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa"))

def replace(txt):
    fins=re.sub(r"\$+|#+","/////",txt)
    return fins
print(replace("$$ start of the program"))
print(replace("number=0, ##poda dai"))
print(replace("queue"))

def convert(phone):
    code=re.sub("(\d{3})-(\d{0,4})-(\d{4})",r"(\1) \2-\3",phone)
    return code
print(convert("My numenr is 222-0000-9089"))
print(convert("My numenr is +222-000-9089"))
print(convert("My numenr is 222-000-9089"))

def website(web):
    ree=r"^https://([\w.]+/[\w./]+)\.aspx$"
    #ree=r"^https://([\w.-]+)/([\w./-]+)\.aspx$"
    fff=re.search(ree,web)
    if fff is None:
        return None
    return fff.group(1)
print(website("https://pip.osourceglobal.com/PIP_PROTIVITI/Login.aspx")) #output: pip.osourceglobal.com
print(website("http://pip.osourceglobal.com/PIP_PROTIVITI/Login.aspx")) #output: none

def converts(spaces):
    rrr=r"\S+"
    sss=re.findall(rrr,spaces)
    return sss
print(converts("My numenr is 222-0000-9089"))

def converts(particular):
    kkk=r"\d{3}-(\d{4})-\d{4}"
    see=re.search(kkk,particular)
    if see is None:
        return None
    return see[1]
print(converts("My numenr is 222-0000-9089"))
print(converts("My numenr is +222-000-9089-123"))
print(converts("My numenr is 222-000-9089"))

#unittestcase
import unittest
class cake():
    def __init__(self, cake_shape=str,cake_size=str):
        self.cake_shape=cake_shape
        self.cake_size=cake_size
        self.cake_topping=[]
        self.price=10 if cake_shape=="round" else 15 if cake_shape=="rectangle" else 7
        self.price+=10 if cake_size=="large" else 7 if cake_size=="medium" else 5
    def cake_toppings(self,toppings=str):
        self.cake_topping.append(toppings)
        self.price+=1
    def cake_ingredients(self):
        ingredients=["sugar","syrup"]
        ingredients.append("cocoa") if self.cake_shape=="round" else ingredients.append ("Vannila syrup")
        ingredients+=self.cake_topping
        return ingredients
    def cake_price(self):
        return self.price

cake_final=cake("round","large")
cake_final.cake_toppings("Ena venalum")
cake_final.cake_toppings("sethuko")
check_ingredients=cake_final.cake_ingredients()
check_price=cake_final.cake_price()

print(check_price, check_ingredients)

class Cake_test(unittest.TestCase):
    def test_cake(self):
        cake_final=cake("round","large")
        cake_final.cake_toppings("Wish")
        cake_final.cake_toppings("Nothing")
        self.assertIn("Wish",cake_final.cake_topping)
        price=cake_final.cake_price()
        self.assertEqual(22,price)
        ingre=cake_final.cake_ingredients()
        self.assertIn("Wish",ingre)
        self.assertIn("sugar",ingre)
        self.assertNotIn("Cccc",ingre)
#unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Cake_test))
if __name__=="__main__":
    unittest.main()

class Library():
    def __init__(self):
        self.collections=[]
    def add_to_collection(self,book):
        self.collections.append(book)
    def check_collection(self, book):
        return book in self.collections
    def show_collection(self):
        return self.collections
li=Library()
li.add_to_collection("poda venna")
li.add_to_collection("puthagam")
print(li.check_collection("poda venna"))
print(li.show_collection())

class li_test(unittest.TestCase):
    
    def test_li(self):
        lib=Library()
        new_book="Poda book"
        lib.add_to_collection(new_book)
        lib.check_collection(lib.check_collection(new_book))
if __name__=="__main__":
    unittest.main()
"""
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

import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
#reg=r"ticky: INFO: ([\w\s]* [\w\d]* [\([\w]*\)])"
reg=r"ticky: INFO: (.+)"
finals=re.search(reg,line)
print(finals)
import operator
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
#print(sorted(fruit.items(),key=operator.itemgetter(0))) #print(sorted(fruit.items()))
# print(sorted(fruit.items(),key=operator.itemgetter(1)))
#print(sorted(fruit.items(),key=operator.itemgetter(0),reverse=True))
print(sorted(fruit.items(),key=operator.itemgetter(1),reverse=True))


