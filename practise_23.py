#multiplication
multiply_number=8
for x in range(1,11):
    result=x* multiply_number
    print(x,"*",multiply_number,"=",result)
#even number
sum=0
for x in range(1,11):
    if x%2==0:
        print(x,"even number")
        sum+=x
print(sum)
#reverse number
reverse_number="121"
reverse_final=""
for x in reverse_number:
    reverse_final=x+reverse_final
print(reverse_final)
#count_digit
count_number_digits=43234324
number_digit=0
while count_number_digits>0:
    count_number_digits=count_number_digits//10
    number_digit+=1
print(number_digit)
#Fizzbuzz
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x,"FizzBizz")
    elif x%3==0:
        print(x,"Fizz")
    elif x%5==0:
        print(x,"Bizz")
    else:
        print(x,"No FizzBizz")
#prime number
sum=0
for x in range(1,11):
    prme=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            prme+=1
    if prme==2:
            print(y)
            sum+=y
print(sum)
#factorial
factorial_number=5
multi_number=1
for x in range(1,factorial_number+1):
    multi_number*=x
print(multi_number)
#pattern number
for x in range(1,9):
    for y in range(1,x+1):
        print("x",end="")
    print()
#Palindrome Check  
palindrome_word="Never odd or even"
palindrome_1=""
palindrome_2=""
palindrome_split=palindrome_word.split()
for x in palindrome_word:
    if x!=" ":
        palindrome_1=x.lower()+palindrome_1
        palindrome_2=palindrome_2+x.lower()
print(palindrome_1,palindrome_2)
if palindrome_2==palindrome_1:
    print(palindrome_word, "pailnd")             
else:
    print(palindrome_word,"Nont")
#Largest digit
largest_digit="54242349543"
digit=0
for x in largest_digit:
    if int(x)>digit:
        digit=int(x)
print(digit)
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
        updated_new=year.replace("2023","2024")
        updated_years.append(updated_new)
    else:
        updated_years.append(year)
print(updated_years)
name=["Keerthi is vasan","Keerthi is raghavan"]
updated_name=[]
for names in name:
    if names.startswith("is",8):
        new_name=names.replace("is","si")
        updated_name.append(new_name)
    else:
        updated_name.append(names)
print(updated_name)
count_letter="54354354355"
letter={}
for x in count_letter:
    if x in letter:
        letter[x]+=1
    else:
        letter[x]=1
print(letter)
FileServer = {"EndUser1": 2.25243, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for end,t in FileServer.items():
    time+=t
print(round(time,3))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
updated_names=[]
for first,last in list_full_names.items():
    for lasts in last:
        full=first+" "+lasts
        updated_names.append(full)
print(updated_names)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
updated_invert={}
for shop,items in invert_resource_dict.items():
    for item in items:
        if item in updated_invert:
            updated_invert[item]+=[shop]
        else:
            updated_invert[item]=[shop]
print(updated_invert)
word_split="Jacki sherrif was a great 1989"
alpha=""
numerical=""
word_place=word_split.split()
for x in word_place:
    if x.isalpha():
        alpha+=x + " "
    else:
        numerical+=x+" "
alpha=alpha.strip()
print("{} at {}".format(alpha,numerical))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
network_updated=""
for domain, num in network.items():
    network_updated+="{} is the id {}".format(domain,num)+"\n"
print(network_updated)
squares_of_numbers=[x*x for x in range(1,11)]
print(squares_of_numbers)
Even_Numbers=[x for x in range(1,11) if x%2==0]
print(Even_Numbers)
condition={x:"even" if x%2==0 else "odd" for x in range(1,11)}
print(condition)
Flatten=[[1, 2], [3, 4], [5, 6]] 
flatten_list=[fill for flat in Flatten for fill in flat]
print(flatten_list)
flatten_list1=[]
for dia in Flatten:
    for dim in dia:
        flatten_list1.append(dim)
print(flatten_list1)
comm1=[1, 2, 3, 4] 
comm2=[3, 4, 5, 6]
kom=[]
for comm in comm1:
    if comm in comm2:
        kom.append(comm)
print(kom)
reverse_list=["hello", "world", "python"]
rev=[kia_list[::-1] for kia_list  in reverse_list]
print(rev)
nnn=[5, 15, 25, 35, 45,54]
for x in nnn:
    if x%5==0:
        b=x+10
        print(b)
word_s="apple banana apple orange banana apple"
word_count_dic={}
word_count=word_s.split()
for x in word_count:
    if x in word_count_dic:
        word_count_dic[x]+=1
    else:
        word_count_dic[x]=1
print(word_count_dic)
square_d={}
for x in range(1,11):
    sq=x*x
    square_d[x]=sq
print(square_d)
invert={"a": 1, "b": 2, "c": 3}
new_invery={}
for a,b in invert.items():
    new_invery[b]=a
print(new_invery)
filter_dic={"a": 5, "b": 15, "c": 8, "d": 20}
filtter={}
for a,b in filter_dic.items():
    if b>5:
        filtter[a]=b
print(filtter)
gr=["apple", "Banana", "apricot", "blueberry", "cherry","kia","bia"]
gr_di={}
for g in gr:
    print(g)
    g_first=g[0].lower()
    if g_first in gr_di:
        gr_di[g_first]+=[g]
    else:
        gr_di[g_first]=[g]
print(gr_di)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nam_det={name:detail for name, detail in zip(names, details)}
print(nam_det)
character_freqs="hello world"
chars={}
#character_freqs=character_freq.split()
for x in character_freqs:
    if x!=" ":
        if x in chars:
            chars[x]+=1
        else:
            chars[x]=1
print(chars)
merge2={"a": 10, "b": 20}
merge1={"b": 5, "c": 15}
merge1_cop=merge1.copy()
for key,value in merge2.items():
    if key in merge1_cop:
        merge1_cop[key]+=value
    else:
        merge1_cop[key]=value
print(merge1_cop)
char_count=["python", "java", "c++"]
char_dic={}
for x in char_count:
    char_len=len(x)
    char_dic[x]=char_len
print(char_dic)
doc={"a": [1, 2], "b": [3, 4], "c": [5]}
ccc=set()
ddd=[]
for a,b in doc.items():
    ccc.update(b)
    ddd.extend(b)
print(ccc)
print(ddd)
#error and handling
my_list = [27, 5, 9, 6, 8]
def RemoveValue(myVal):
    my_list.remove(myVal)
    
    return my_list
print(RemoveValue(27))
#print(RemoveValue(27))

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
import random
def check_partipant(participants):
    save_participants={}
    for participant in participants:
            save_participants[participant] = random.randint(1, 9)
    try:
            if "Ranga" in save_participants:
                if save_participants["Ranga"] == 8:
                    return True
            else:
                raise KeyError("Name is not present")
    except KeyError as e:
            print(e)
            return None
participants=["Keerthivasan","Rajesh","Lokesh","Logesh"]
print(check_partipant(participants))
"""
import unittest
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
"""
