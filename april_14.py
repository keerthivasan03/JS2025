#multiplication
def multi(n):
    for x in range(1,n+1):
        result=x*n
        print(x,"*",n, "=", result)
multi(8)
#sum_of_even
sum=0
for x in range(1,11):
    if x%2==0:
        print(x,"Is a even number")
        sum+=x
print(sum)
#reverse
number="4342312364565"
store_number=""
for x in number:
    store_number=x+store_number
print(store_number)
#count digits
count_digit=754785743
saver=0
while count_digit>0:
    count_digit=count_digit//10
    saver+=1
print(saver)
#If elif
for x in range(1,16):
    if x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Bizz")
    elif x%3 ==0 and x%5==0:
        print(x, "Fizz Bizz")
    else:
        print(x, "No FizzBizz")
#prime
po=0
for x in range(1,16):
    s=0
    for y in range(1,x+1):
        if x%y==0 and y!=0:
            s+=1
    if s==2:
        print(y)
        po+=y
print(po)
#factorial
def fact(n):
    mu=1
    for x in range(1,n+1):
        mu*=x
    print(mu)
fact(5)
#pattern
def pyra(n):
    for x in range(1,n+1):
        for y in range(1,x+1):
            print("X",end="")
        print()
pyra(8)
#palindrome
palin="121"
store_palin=""
for x in palin:
    store_palin=store_palin+x
print(store_palin)
if store_palin==palin:
    print(palin,"Is a palindrome")
#largest dgit
larger="7542432"
comp=1
for x in larger:
    if int(x)>comp:
        comp=int(x)
print(comp)
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
new_year=[]
for year in years:
    if year.endswith("2023"):
        new=year.replace("2023","2024")
        new_year.append(new)
    else:
        new_year.append(year)
print(new_year)
updated_years1=[year1.replace("2025", "2024") if year1.endswith("2025") else year1 for year1 in years ]
print(updated_years1)
#count
count_letter="580927498738574354543"
count_dic={}
for x in count_letter:
    if x in count_dic:
        count_dic[x]+=1
    else:
        count_dic[x]=1
print(count_dic)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
totat=0.0
for key,value in FileServer.items():
    totat+=value
print(round(totat,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
new_name=[]
for key,value in list_full_names.items():
    for values in value:
        n=key+" "+values
        new_name.append(n)
print(new_name)
#swap
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
new_invert={}
for key,value in invert_resource_dict.items():
    for values in value:
        if values in new_invert:    
            new_invert[values]+=[key]
        else:
            new_invert[values]=[key]
print(new_invert)
#words update
word_place="Jacki sherrif was a great 1989"
word_split=word_place.split()
alpha=""
numeric=""
for x in word_split:
    if x.isalpha():
        alpha+=x+" "
    else:
        numeric+=x+""
alpha=alpha.strip()
print("{} is a great {}".format(alpha,numeric))
#continu
coninye={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
for key,value in coninye.items():
    print("{} is the id {}".format(key,value)+"\n")
#word_palindrome
word="Never odd or even"
new_word1=""
new_word2=""
word_spl=word.split()
for x in word:
    if x!=" ":
        new_word1=x.lower()+new_word1
        new_word2=new_word2+x.lower()
print(new_word1)
print(new_word2)
if new_word1==new_word2:
    print(word, "Is a palindrome")
else:
    print(word,"Not a palndrome")
#word 
word_place1="Jacki sherrif was a great 1989 at 1230"
output=[]
word_spll=word_place1.split()
for x in word_spll:
    output.append(x)
    if x.isalpha():
        if x=="was":
            output.append("mass maharaja")
        elif x=="great":
            output.append("Nala irupa")
    if x.isnumeric():
        if x=="1989":
            output.append("was a golden year")
        elif x=="1230":
            output.append("")  
output1=" ".join(output)
print(output1)
#particular reverse
reverse="Keerthivasan is not good at coding"
wreverse=reverse[12:24]
new_u=reverse[:13]+wreverse[::-1]+reverse[24:]
print(new_u)
reverse_new="Keerthivasan is not good at coding"
save=""
for x in reverse_new:
    save=x[13:23]+save
    nnn=(reverse_new[:13]+save+reverse_new[24:])
print(nnn)
squ=[x*x for x in range(1,11)]
print(squ)
eve=["even" if x%2==0 else "odd" for x in range(1,11) ]
print(eve)
eve1={x:"even" if x%2==0 else "Odd" for x in range(1,11)}
print(eve1)
numer=[x for x in range(1,11) if x%2==0  ]
print(numer)
condition=["even" if x%2==0 else "odd" for x in range(1,11)]
print(condition)
lists= [[1, 2], [3, 4], [5, 6]] 
new_l=[]
for l in lists:
    for q in l:
        new_l.append(q)
print(new_l)
#update_liyy
#import itertools
nested_list = [1, [2, [3, 4]], 5]
def flatten_itertools(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_itertools(item))
        else:
            result.append(item)
    return result
flattened_list = list(flatten_itertools(nested_list))
print(flattened_list)
#updates
u1=[1, 2, 3, 4] 
u2=[3, 4, 5, 6]
for x in u1:
    if x in u2:
        print(x)
#common
re=["hello", "world", "python"]
re_c={}
for x in re:
    lens=len(x)
    re_c[x]=lens
print(re_c)
re_l=[rr[::-1] for rr in re]
print(re_l)
#fil
filter_transform=[5, 15, 25, 35, 45,12]
for x in filter_transform:
    if x%5==0:
        x=x+10
        print(x)
#word_fre
fruits="apple banana apple orange banana apple"
fruit_split=fruits.split()
fruit_dic={}
for x in fruit_split:
    if x in fruit_dic:
        fruit_dic[x]+=1
    else:
        fruit_dic[x]=1
print(fruit_dic)
#sq_dic
sq_dic={}
for x in range(1,11):
    res=x*x
    sq_dic[x]=res
print(sq_dic)
#inverted value
inv_dic={"a": 1, "b": 2, "c": 3}
new_inv_dic={}
for key,value in inv_dic.items():
    new_inv_dic[value]=key
print(new_inv_dic)
#filter dic
n_filter={"a": 5, "b": 15, "c": 8, "d": 20}
update_fil={}
for key,value in n_filter.items():
    if value>5:
        update_fil[key]=value
print(update_fil)
#group by first letter
gbf=["apple", "banana", "apricot", "blueberry", "cherry"]
bgf_dic={}
for x in gbf:
    firt=x[0]
    if firt in bgf_dic:
        bgf_dic[firt]+=[x]
    else:
        bgf_dic[firt]=[x]
print(bgf_dic)
#zip
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
update_name={name:detail for name,detail in zip(names,details)}
print(update_name)
#character frequency
character="hello world"
character_dic={}
character=character.upper()
for x in character:
    if x!=" ":
        if x in character_dic:
            character_dic[x]+=1
        else:
            character_dic[x]=1
print(character_dic)
#merge dic
import copy
merge1={"a": 10, "b": 20}
merge2={"b": 5, "c": 15}
merge1c=copy.deepcopy(merge1)
for key,value in merge2.items():
    if key in merge1c:
        merge1c[key]+=value
    else:
        merge1c[key]=value
print(merge1c, merge1, merge2)
#copy
import copy
merge3={"a": 10, "b": 20}
merge4={"b": 5, "c": 15}
merge3c=copy.copy(merge3)
for key,value in merge4.items():
    if key in merge3c:
        merge3c[key]+=value
    else:
        merge3c[key]=value
print(merge3c, merge3, merge4)
#combine
li_di={"a": [1, 2], "b": [3, 4], "c": [5]}
lis=[]
dic=set()
for key,value in li_di.items():
    lis.extend(value)
    dic.update(value)
print(lis)
print(dic)
#instance
li_di1=[[1, 2], [3, 4], [5, 6]] 
li_di11=[]
for x in li_di1:
    if isinstance(x,list):
        li_di11.extend(x)
    else:
        li_di11.append(x)
print(li_di11)
#interview cursion
recus=[1, [2, [3, 4]], 5]
recus_output=[]
def flatten(new_list):
    for item in new_list:
        if isinstance(item,list):
            flatten(item)
        else:
            recus_output.append(item)
flatten(recus)
print(recus_output)
#interview_2
name="Keerthi vasan"
name=name.upper()
vowel="AEIOU"
vwel_dic={}
sums=0
for names in name:
    if names in vowel:
        sums+=1
print(sums)
for nami in name:
    if nami!=" ":
        if nami not in vowel:
            if nami not in vwel_dic:
                vwel_dic[nami]=1
            else:
                vwel_dic[nami]+=1
print(vwel_dic)
input_str = "Ram:89,Lakshman:75,Hanuman:92"
input_dic={}
sum=0
person=""
for name in input_str.split(","):
    k,v=name.split(":")
    input_dic[k]=v
print(input_dic)
if int(v)>sum:
    sum=int(v)
    person=k
print(person,sum)
#sorting
list1 = [1, 7, 3, 4, 2 ,12, 5, 6]
length=len(list1)
for x in range(length-1):
    for y in range(length-x-1):
        if list1[y]> list1[y+1]:
            list1[y],list1[y+1]=list1[y+1],list1[y]
print(list1)
list11=copy.deepcopy(list1)
list11[0], list11[-1]=list11[-1], list11[0]
print(list11)
#default sort
list2 = [1, 7, 3, 4, 2 ,12, 5, 6]
list2.sort()
print(list2)
list3 = [1, 7, 3, 4, 2 ,12, 5, 6]
list3_sort=sorted(list3)
print(list3_sort)
#searching
def liner(key,value):
    for i,x in enumerate(key):
        if x==value:
            return i 
    return -1
reuult=liner(["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor","Keerthi"],"Cameron")
print(reuult)

List1 = [{'emp': 'John', 'dept no.': 12}, [{'emp': 'Adam', 'dept no.': 5}]]
for record in List1:
    if isinstance(record,dict):
        output=[]
        for key,value in record.items():
            output.append(f"{key} is {value}")
        print(" and ".join(output))
    elif isinstance(record,list):
        output=[]
        for sunrecord in record:    
            for key,value in sunrecord.items():
                output.append(f"{key} is {value}")
            print(" and ".join(output))

List12 = [{'emp': 'John', 'dept no.': 12}, {'emp': 'Adam', 'dept no.': 5}]
for record in List12:
    output=[]
    for key,value in record.items():
        output.append(f"{key} is {value}")
    print(" and ".join(output))

#regex
import re
def code_red(rege):
    first_regex=re.findall(r"\w*",rege)
    resul=[]
    for second in first_regex:
        second_regex=re.findall(r"[AEIOUaeiou]",second)
        if len(second_regex)>=3:
            resul.append(second)
    return resul
print(code_red("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa keerthi"))

#isalpha check
input_str = "KeerthiVasan123"
# Pick only alphabets and reverse
filtered = ''.join([ch for ch in input_str if ch.isalpha()])
reversed_str = filtered[::-1]
print(reversed_str)

oist1 = [{'emp': 'John', 'dept no.': 12}, [{'emp': 'Adam', 'dept no.': 5}]]
for record in oist1:
    if isinstance(record,dict):
        ob=[]
        for key,value in record.items():
            ob.append(f"{key} is {value}")
        print(" and ".join(output))
    elif isinstance(record,list):
        ob=[]
        for subrecord in record:
            for key,value in subrecord.items():
                ob.append(f"{key} is {value}")
            print(" and ".join(ob))

class Bird:
    def sound(self):
        print("Some bird sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says Hello!")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

# Polymorphism
for bird in [Parrot(), Sparrow()]:
    bird.sound()




