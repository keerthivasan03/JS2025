import csv
import re
import unittest
"""file_location="C:\\Users\\keerthivasan.a\\Book_1.csv"
with open (file_location,"r") as readings:
    #readings1=csv.reader(readings)
    readings1=csv.DictReader(readings)
    for row in readings1:
        name, username, department = row
        print("name: {}, username={}, department={}".format(name, username,department
        print("name: {}, username={}, department={}".format(row["name"], row["username"], row["department"]))
file_location1="C:\\Users\\keerthivasan.a\\Book_7.csv"
data=[["Name", "Department", "Salary"],
["Aisha Khan", "Engineering", "80000"],
["Jules Lee", "Marketing", "67000"],
["Queenie Corbit", "Human Resources", "90000"]]
with open (file_location1,"w",newline="") as writings1:
    writers=csv.writer(writings1)
    writers.writerows(data)
file_location2="C:\\Users\\keerthivasan.a\\Book_8.csv"
csv.register_dialect("practise",delimiter="|",quotechar="'",strict=True,skipinitialspace=True)
data1=[{"Name":"Aisha Khan", "Department":"     Engineering", "Salary":"80000"},{"Name":"Jules Lee", "Department":"Marketing", "Salary":"67000"},
      {"Name":"Queenie Corbit", "Department":"Human Resources", "Salary":"90000"}]
fields=["Name","Department","Salary"]
with open(file_location2,"w",newline="") as di:
    dict=csv.DictWriter(di,fieldnames=fields, dialect="practise")
    dict.writeheader()
    dict.writerows(data1)
with open(file_location2,"r") as ki:
    dic1=csv.DictReader(ki,dialect="practise")
    #dic1.reader(ki)
    for rows in dic1:
        print("Name:{},Department:{},Salary:{}".format(rows["Name"],rows["Department"], rows["Salary"]))

print(re.search(r"ab","newabas"))
log = "July 31 07:51:48 mycomputer bad_process[123455354]: ERROR Performing package upgrade"
result=re.search(r"\[(\d+)\]",log)
print(result.group(1))
print(re.search(r"wash","new washing machine",re.IGNORECASE))
print(re.search(r"[aA]","bada"))
print(re.search("cat|Dog", "Love for DoG",re.IGNORECASE))
print(re.search(r"ki.*a","kiaMia"))
ioo1=re.search(r"p+r+", "python porgramming")
print(ioo1)
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome.com"))
print(re.search("\w*","Welcome_home"))
print(re.search(r"^A.*a$", "Azerbaiga"))
print(re.search(r"^[A-Z][a-z\s]*[!.?]$","Is this is a sentence?"))
def rearrange_nae(text):
    res=re.search(r"^([\w]+), ([\w \.]+)$", text)
    #(r"^([\w\s]+),\s([\w\s\.]+)$"
    if res== None:
        return None
    return "{} {}".format(res[2],res[1])
print(rearrange_nae("Hopper, Grace M."))
def transform(new_text):
    formation=re.sub(r"(\d{3}-\d{3}-\d{4})",r"+1-\1",new_text)
    return formation
print(transform("Sabarina,802-867-0000,system admini"))
def kk(its_time1):
    vowel1=re.findall(r"(\b\w*([aeiouAEIOU]){3,}\w*\b)",its_time1)
    #vowel1 = re.findall(r"\b\w*(?:[aeiouAEIOU].*?){3,}\w*\b", its_time)
    #[aeiouAEIOU].*?)
    return vowel1
print(kk("Obviously, great person ever keeerthoi seen in my life, beautiful beautiful"))
def kkk(its_time):
    # Use this regular expression to capture words with at least 3 vowels
    vowel = re.findall(r"\b\w*(?:[aeiouAEIOU][\w]*){3,}\b", its_time)
    return vowel

print(kkk("Obviously, great person ever keerthoi seen in my life, beautiful beautiful"))
def rearrange_name(text):
    refernce=re.search(r"^([A-Za-z]*),([A-Za-z\s]*)",text)
    return "{},{}".format(refernce[2], refernce[1])
print(rearrange_name("Lovelace, Ada")) """

class cake_check:
    def __init__(self,cake_size=str,cake_shape=str):
        self.cake_shape=cake_shape
        self.cake_size=cake_size
        self.cake_topping=[]
        self.price=10 if cake_shape=="large" else 8 if cake_shape=="small" else 6
        self.price+=6 if cake_size=="90" else 4 if cake_size=="60" else 2
    def cake_toppings(self, toppings=str ):
        self.cake_topping.append(toppings)
        self.price+=1
    def cake_items(self):
        items=["maida","sugar", "syrup"]
        items.append("cocoa") if self.cake_shape=="large" and self.cake_size=="90" else "choco" if self.cake_shape=="small" and self.cake_size=="60" else "Nothing"
        items+=self.cake_topping
        return items
    def check_price(self):
        return self.price
cake=cake_check("90","large")
cake.cake_toppings("Bhaiya")
cake.cake_toppings("Ogaya")
cake_ingedients=cake.cake_items()
cake_price=cake.check_price()
print(cake_ingedients,cake_price)

class Testcasefactory(unittest.TestCase):
    def test_price(self):
        cake=cake_check("90","large")
        price = cake.check_price()
        self.assertEqual(price,16)

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Testcasefactory))

class library:
    def coll(self):
        self.collection=[]
    def add_new_book(self,book_title):
        self.collection.append(book_title)
    def presence(self,book_title):
        return book_title in self.collection
class testlibra(unittest.TestCase):
    def test_book_present(self):
        li=library()
        li.add_new_book("Book")
        self.assertTrue(li.presence("Book"))
    if __name__=="__main__":
        unittest.main(argv=[''],exit=False)

class Lobrary:
    def library_collection(self):
        self.collections=[]
    def add_collection(self, book_title):
        self.collections.append(book_title)
    def has_collection(self,book_title):
        return book_title in self.collections()
class TestLibroray(unittest.TestCase):
    def test_book(self):
        leo=Lobrary()
        leo.add_collections("has harry")
        self.assertTrue(leo.has_collection("has harry"))
    
if __name__=="__main__":
    unittest.main(argv=[''],exit=False)


