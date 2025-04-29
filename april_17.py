#multiply
def mul(n):
    for x in range(1,n+1):
        res=x*n
        print (n,"x",x,"=",res)
#sum
sums=0
for x in range(1,11):
    if x%2==0:
        print(x)
        sums+=x
print(sums)
#reverese
number="4342312364565"
num_rev="" 
for x in number:
    num_rev=x+num_rev
print(num_rev)
##count digits
count_digit=754785743
digit_incre=0
while count_digit>0:
    count_digit=count_digit//10
    digit_incre+=1
print(digit_incre)
#If elif
for x in range(1,11):
    if x%3==0:
        print(x,"Fizz")
    elif x%5==0:
        print(x, "Bizz")
    elif x%3==0 and x%5==0:
        print(x,"FizzBizz")
    else:
        print(x, "No divisible")
#prime
sumss=0
for x in range(1,11):
    prm=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            prm+=1
    if prm==2:
        print(y)
        sumss+=y
print(sumss)
#factorial
def fact(n):
    ff=1
    for x in range(1,n+1):
        ff*=x
    print(ff)
fact(5)
#pattern
for x in range(1,9):
    for y in range(1,x+1):
        print("x",end="")
    print()
#palindrome
palin="121"
new_palin=""
for x in palin:
    new_palin=x+new_palin
print(new_palin)
larger="7542432"
l=0
for x in larger:
    if int(x)>l:
        l=int(x)
print(l)
#year
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
new_year=[]
for x in years:
    if x.endswith("2023"):
        n=x.replace("2023","2024")
        new_year.append(n)
    else:
        new_year.append(x)
print(new_year)
updated_year=[year.replace("2024","2025") if year.endswith("2024") else year for year in years]
print(updated_year)
#count
count_letter="580927498738574354543"
cou={}
for x in count_letter:
    if x in cou:
        cou[x]+=1
    else:
        cou[x]=1
print(cou)
FileServer = {"EndUser1": 2.8577, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
tot=0.0
for key,value in FileServer.items():
    tot+=value
print(round(tot,1))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
full=[]
for key,value in list_full_names.items():
    for values in value:
        new_name=key+" "+values
        full.append(new_name)
print(full)
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
alpha=""
num=""
word_place=word_place.split()
for x in word_place:
    if x.isalpha():
        alpha+=x+" "
    else:
        num+=x+" "
alpha=alpha.strip()
print(f"{alpha} is a great actor {num}")
#continu
coninye={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
for key,value in coninye.items():
    print(f"{key} id is {value}"+("\n"))
#word_palindrome
word="Never odd or even"
word1=""
word2=""
word=word.lower()
for x in word:
    if x!=" ":
        word1=x+word1
        word2=word2+x
print(word2)
print(word1)
if (word1==word2):
    print(word, " Is a palindrome")
else:
    print(word, " Is not a palindrome")
#word 
word_place1="Jacki sherrif was a great 1989 at 1230"
output=[]
word_p=word_place1.split()
for x in word_p:
    output.append(x)
    if x.isalpha():
        if x=="was":
            output.append("great news")
        elif x=="great":
            output.append("not great")
    if x.isnumeric():
        if x=="1989":
            output.append("g")
        elif x=="1230":
            output.append("n")
print(" ".join(output))
#particular reverse
reverse="Keerthivasan is not good at coding"
particular_rev=reverse[13:20]
update_p=""
for x in particular_rev:
    update_p=x+update_p
print(update_p)
new_rec=reverse[:13]+update_p+reverse[20:]
print(new_rec)
new_rec1=reverse[:13]+particular_rev[::-1]+reverse[20:]
print(new_rec1)
#square
sq=[x*x for x in range(1,11)]
print(sq)
#even
eve=["even" if x%2==0 else "odd" for x in range(1,11)]
print(eve)
#dic
evv={x:"even" if x%2==0 else "odd" for x in range(1,11)}
print(evv)
#even
new_eve=[x  for x in range(1,11) if x%2==0]
print(new_eve)
#nested
lists= [[1, 2], [3, 4], [5, 6]] 
n_l=[]
for x in lists:
    for y in x:
        n_l.append(y)
print(n_l)

nested_list = [1, [2, [3, 4]], 5]
def fals(li):
    nn=[]
    for item in li:
        if isinstance(item, list):
            nn.extend(fals(item))
        else:
            nn.append(item)
    return nn
new_nn=fals(nested_list)
print(new_nn)
#updates
u1=[1, 2, 3, 4] 
u2=[3, 4, 5, 6]
for x in u1:
    if x in u2:
        print(x)
#common
re=["hello", "world", "python"]
ne_d={}
for x in re:
    lens=len(x)
    ne_d[x]=lens
    neww=x[::-1]
    print(neww)
print(ne_d)
re_l=[rr[::-1] for rr in re]
print(re_l)
#f
filter_transform=[5, 15, 25, 35, 45,12]
for x in filter_transform:
    if x%5==0:
        x=x+10
        print(x)
#word_count
fruits="apple banana apple orange banana apple"
fruits1=fruits.split()
fruits_d={}
for x in fruits1:
    if x in fruits_d:
        fruits_d[x]+=1
    else:
        fruits_d[x]=1
print(fruits_d)
#sq_dic
sq_dic={}
for x in range(1,11):
    r=x*x
    sq_dic[x]=r
print(sq_dic)
#inverted value
inv_dic={"a": 1, "b": 2, "c": 3}
nnn={}
for key,value in inv_dic.items():
    nnn[value]=[key]
print(nnn)
#filter dic
n_filter={"a": 5, "b": 15, "c": 8, "d": 20}
nn_filter={}
for key,value in n_filter.items():
    if value>5:
        nn_filter[key]=value
print(nn_filter)
#group by first letter
gbf=["apple", "banana", "apricot", "blueberry", "cherry"]
gbf_dic={}
for x in gbf:
    x_o=x[0]
    if x_o in gbf_dic:
        gbf_dic[x_o]+=[x]
    else:
        gbf_dic[x_o]=[x]
print(gbf_dic)
#zip
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nd={name:detail for name,detail in zip(names,details)}
print(nd)
#character frequency
character="hello world"
character_dic={}
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
new_merge=copy.deepcopy(merge1)
for key,value in merge2.items():
    if key in new_merge:
        new_merge[key]+=value
    else:
        new_merge[key]=value
print(new_merge)
#combine
li_di={"a": [1, 2], "b": [3, 4], "c": [5]}
lis=[]
dic=set()
for key,value in li_di.items():
    lis.extend(value)
    dic.update(value)
print(lis, dic)
#instance
li_di1=[[1, 2], [3, 4], [5, 6]] 
ll=[]
for x in li_di1:
    if isinstance(x,list):
        ll.extend(x)
    else:
        ll.append(x)
print(ll)
#interview cursion
recus=[1, [2, [3, 4]], 5]
recus_output=[]
def flatten(li):
    for x in li:
        if isinstance(x,list):
            flatten(x)
        else:
            recus_output.append(x)
flatten(recus)
print(recus_output)
#interview_2
name="Keerthi vasan"
vowel="aeiou"
name_lower=name.lower()
s=0
vowel_dic={}
for x in name_lower:
    if x in vowel:
        s+=1
        if x in vowel_dic:
            vowel_dic[x]+=1
        else:
            vowel_dic[x]=1
print(s)
print(vowel_dic)
input_str = "Ram:89,Lakshman:75,Hanuman:92"
input_dic={}
sum=0
person=""
for x in input_str.split(","):
    k,v=x.split(":")
    input_dic[k]=v
print(input_dic)
if int(v)>sum:
        sum=int(v)
        person=k
print(person,sum)
#sorting
list1 = [1, 7, 3, 4, 2 ,12, 5, 6]
so=len(list1)
for x in range(so-1):
    for y in range(so-x-1):
        if list1[y]>list1[y+1]:
            list1[y],list1[y+1]=list1[y+1],list1[y]
print(list1)
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)
#search
def liner(key,value):
    for i, x in enumerate(key):
        if x==value:
            return i, x
    return -1

reuult=liner(["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor","Keerthi"],"Cameron")
print(reuult)

List1 = [{'emp': 'John', 'dept no.': 12}, [{'emp': 'Adam', 'dept no.': 5}]]
for rr in List1:
    output=[]
    if isinstance(rr,dict):    
        for key,value in rr.items():
            output.append(f"{key} is {value}")
        print(" and ".join(output))
    elif isinstance(rr,list):
        output=[]
        for rrr in rr:
            for key,value in rrr.items():
                output.append(f"{key} is {value}")
        print(" and ".join(output))

nlist1 = [{'emp': 'John', 'dept no.': 12}, {'emp': 'Adam', 'dept no.': 5}]

for rrr in nlist1:
    output=[]
    for key,value in rrr.items():
        output.append(f"{key} is {value}")
    print(" and ".join(output))
import re
def code_red(red):
    first=re.findall(r"\w*",red)
    print(first)
    resu=[]
    for second in first:
        find=re.findall(r"[aeiouAEIOU]",second)
        if len(find)>3:
            resu.append(second)
    return resu
print(code_red("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa keerthi"))

#reverse1
kee="keerthivasan123"
o=""
for keer in kee:
    if keer.isalpha():
        o+=keer
print(o)
res=o[::-1]
print(res)




def reverse_string_preserve_whitespace(s):
    # Step 1: Collect all non-space characters in reverse order
    reversed_chars = ''
    for c in reversed(s):
        if c != ' ':
            reversed_chars += c

    # Step 2: Rebuild the string, placing characters or spaces accordingly
    result = ''
    index = 0  # index for reversed_chars
    for c in s:
        if c == ' ':
            result += ' '
        else:
            result += reversed_chars[index]
            index += 1

    return result

# Example usage
input_str = "Keerthi vasab"
output_str = reverse_string_preserve_whitespace(input_str)
print(f"Input:  '{input_str}'")
print(f"Output: '{output_str}'")

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # From parent class
d.bark()   # From child class

sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for item in sample_data:
    if item != ():
        print(item)
    if isinstance(item,tuple):
        if len(item)>0:
            print(item)

str1="Listen"
str2="Silent"
if (sorted(str1.lower())==sorted(str2.lower())):
    print("Is Anagram")
else:
    print("Is not Anagram")

#with inbuilt
str3= 'Keer$%$^$%&^%t^^i'
aq=""
asa=""
for st in str3:
    if st.isalpha():
        aq+=st
for asz in aq:
    asa=asz+asa
print(asa)

#without inbuilt
stack=[]
for ch in str3:
    if ("a"<=ch<="z") or ("A"<=ch<="Z"):
        stack.append(ch)
print(stack)
result=""
#while stack:
while len(stack)>0:
    result+=stack.pop()
print(result)

#remove duplicate
str="Keertthii"
result=""
duplicate=set()
for charact in str:
    if charact not in duplicate:
        duplicate.add(charact)
        result+=charact
print(result)


def log(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@log
def greet():
    print("Hi")

greet()
#swap
st={'a':3,'b':4,'c':9}
new_st={'a':st["b"],'b':st["c"],'c':st["a"]}
print(new_st)
#number multiply
st = "a2b10c1"
output = ""
i = 0

while i < len(st):
    char = st[i]          # Take the letter
    i += 1
    num = ""              # To store digits

    while i < len(st) and st[i].isdigit():   # Check if next characters are numbers
        num += st[i]
        i += 1

    output += char * int(num)   # Repeat the character

print(output)
#middleletter
middle="Keerthivasa"
mid=len(middle)//2
if len(middle)%2==0:
    results= middle[mid-1:mid+1]
else:
    results= middle[mid]
print(results)
#multiply
"""muls="Keerthi789vasa"
alpha=""
beta=""
prox=1
for muld in muls:
    if muld.isnumeric():
        beta+=muld
    else:
        alpha+=muld
for d in beta:
    prox*=int(d)
print(f"{alpha}{prox}")"""
muls = "Keerthi789vasa"
alpha = ""
beta = ""
prox = 1

# Loop through the string and separate alphabets and digits
for muld in muls:
    if muld.isnumeric():
        beta += muld  # Collect numeric characters in 'beta'
    else:
        alpha += muld  # Collect non-numeric characters in 'alpha'

# Multiply all digits found in 'beta'
for digit in beta:
    prox *= int(digit)

# Combine the parts: alphabets + product of digits + remaining string
remaining = muls[len(alpha)+len(beta):]

# Print the final output
print(f"{alpha}{prox}{remaining}")

