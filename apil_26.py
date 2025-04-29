multi=8
for x in range(1,multi+1):
    result=multi*x
    print(multi ,"X", x, "=", result)
su=0
for x in range(1,11):
    if x%2==0:
        print(x,"Is Even")
        su+=x
print(su)
reverse_number="1244314"
reverse_number_s=""
for x in reverse_number:
    reverse_number_s=x+reverse_number_s
print(reverse_number_s)
counter=423423
cou=1
while counter>0:
    counter=counter//10
    cou+=1
print(cou)
for x in range(1,11):
    if x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Buzz")
    elif x%3==0 and x%5==0:
        print(x, "FizzBizz")
    else:
        print(x,"No FizzBuzz")
ss=0
for x in range(1,11):
    pp=0
    for y in range(1,x+1):
        if x%y==0 and y!=0:
            pp+=1
    if pp==2:
        print(y, "is prime number")
        ss+=y
print(ss)
fac=5
mm=1
for x in range(1,fac+1):
    mm*=x
print(mm)
for x in range(1,9):
    for y in range(1,x+1):
        print("X", end="")
    print()
#pp="Never odd or even"
pp="12121"
pp1=""
pp2=""
for x in pp.lower():
    if x!=" ":    
        pp1=x+pp1
        pp2=pp2+x
print(pp1, pp2)
if pp1==pp2:
    print(pp,"Is palindrome")
else:
    print(pp,"Is not palindrome")
ll="413497943"
l=0
for x in ll:
    if int(x)>l:
        l=int(x)
print(l)
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
uo=[year.replace("2023","2024") if year.endswith("2023") else year for year in years]
print(uo)
ui=[]
for year in years:
    if year.endswith("2024"):
        n=year.replace("2024","2025")
        ui.append(n)
    else:
        ui.append(year)
print(ui)
count_letter="5435435435"
c={}
for x in count_letter:
    if x in c:
        c[x]+=1
    else:
        c[x]=1
print(c)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
tt=0.0
for x,valu in FileServer.items():
    tt+= valu
print(round(tt,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
nq=[]
for x,y in list_full_names.items():
    for ys in y:
        nn=x+" "+ys
        nq.append(nn)
print(nq)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
inv_dic={}
for x,y in invert_resource_dict.items():
    for yy in y:    
        if yy in inv_dic:
            inv_dic[yy]+=[x]
        else:
            inv_dic[yy]=[x]
print(inv_dic)
word_place="Jacki sherrif was a great 1989"
lpha=""
bta=""
word_place_sp=word_place.split()
for x in word_place_sp:
    if x.isalpha():
        lpha+=x+" "
    else:
        bta+=x
lpha=lpha.strip()
print(f"{lpha} is is is {bta}")
word_place1="Jacki sherrif was a great 1989 to 1999"
out=[]
word_places=word_place1.split()
for x in word_places:
    out.append(x)
    if x.isalpha():
        if x=="was":
            out.append("great")
    else:
        if x=="1999":
            out.append("till 2000")
print(" ".join(out))
number_mul="Keerthi789vsan"
oo=1
mm=number_mul[7:10]
print(mm)
for x in mm:
    oo*=int(x)
print(oo)
numo=number_mul[:7]+str(oo)+ number_mul[10:]
print(numo)
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
for x,y in network.items():
    print(f"{x} is {y}"+"\n")
sq=[x*x for x in range(1,11)]
print(sq)
ex=[x for x in range(1,11) if x%2==0 ]
print(ex)
con=["even" if x%2==0 else "odd" for x in range(1,11)]
print(con)
con1={x:"even" if x%2==0 else "odd" for x in range(1,11)}
print(con1)
fl=[[1, 2], [3, 4], [5, 6]]
n_fl=[y for x in fl for y in x]
print(n_fl)
n1=[1, 2, 3, 4]
n2=[3, 4, 5, 6]
n3=[]
for n in n2:
    if n in n1:
        n3.append(n)
print(n3)
re=["hello", "world", "python"]
re1=""
for x in re:
    re1=x[::-1]
    print(re1)
re2="keerthivasan A","SDET"
re3=""
for x in re2:
    re3=x[::-1]
    print(re3)
m=[5, 15, 25, 35, 45,33]
for x in m:
    if x%5==0:
        n=x+10
        print(n)
word_f="apple banana apple orange banana apple"
wor=word_f.split()
wo_d={}
for x in wor:
    if x in wo_d:
        wo_d[x]+=1
    else:
        wo_d[x]=1
print(wo_d)
squ={}
for x in range(1,11):
    e=x*x
    squ[x]=e
print(squ)
ii={"a": 1, "b": 2, "c": 3}
ii1={"a":ii["c"],"b":ii["a"],"c":ii["b"]}
print(ii1)
ii2={}
for x, y in ii.items():
    ii2[y]=x
print(ii2)
io={"a": 5, "b": 15, "c": 8, "d": 20}
io1={}
for x,y in io.items():
    if y>5:
        io1[x]=y
print(io1)
gh="apple", "banana", "apricot", "blueberry", "cherry"
gh_d={}
for x in gh:
    gf=x[0]
    if gf in gh_d:
        gh_d[gf]+=x
    else:
        gh_d[gf]=x+" "
print(gh_d)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nd_dic={name:detail for name,detail in zip(names,details)}
print(nd_dic)
kj="hello world"
kj_d={}
for x in kj:
    if x!=" ":
        if x in kj_d:    
            kj_d[x]+=1
        else:
            kj_d[x]=1
print(kj_d)
m={"a": 10, "b": 20}
o={"b": 5, "c": 15}
m1=m.copy()
for x,y in o.items():
    if x in m1:
        m1[x]+=y
    else:
        m1[x]=y
print(m1)
gg=["python", "java", "c++"]
k_dic={}
for k in gg:
    qa=len(k)
    k_dic[k]=qa
    print(k_dic)
lo={"a": [1, 2], "b": [3, 4], "c": [5]}
lk=set()
for a,b in lo.items():
    lk.update(b)
print(lk)
nest=[[1, 2], [3, 4], [5, 6]]
bn=[]
for x in nest:
    for y in x:
        bn.append(y)
print(bn)
recus=[1, [2, [3, 4]], 5]
nestt=[]
def flatten(l):
    for x in l:
        if isinstance(x,list):
            flatten(x)
        else:
            nestt.append(x)
flatten(recus)
print(nestt)
name="Keerthi vasan"
vowel="aeiou "
new={}
s=0
for x in name:
    if x in vowel:
        if x!=" ": 
            s+=1   
            if x in new:
                new[x]+=1
            else:
                    new[x]=1
print(new)
print(s)
input_str = "Ram:89,Lakshman:75,Hanuman:92"
val=0
nam=""
input_dic={}
for x in input_str.split(","):
    k,v=x.split(":")
    input_dic[k]=v
if int(v)>val:
    val=int(v)
    nam=k
print(f"{nam}:{val}")
print(input_dic)
list1 = [1, 7, 3, 4, 2 ,12, 5, 6]
nnn=len(list1)
for x in range(nnn-1):
    for y in range(nnn-x-1):
        if list1[y]>list1[y+1]:
            list1[y],list1[y+1]=list1[y+1],list1[y]
print(list1)    
def liner(key,value):
    for i,x in enumerate(key):
        if x==value:
            return x,i
    return -1
reuult=liner(["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor","Keerthi"],"Cameron")
print(reuult)
qist1 = [{'emp': 'John', 'dept no.': 12}, [{'emp': 'Adam', 'dept no.': 5}]]
for ll in qist1:
    op=[]
    if isinstance(ll,dict):
        for x,y in ll.items():
            op.append(f"{x} is {y}")
            print(" and ".join(op))
    elif isinstance(ll,list):
        op=[]
        for lll in ll:
            for x,y in lll.items():
                op.append(f"{x} is {y}")
        print(" and ".join(op))    
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
km=code_red("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa keerthi")
print(km)

kee="keerthivasan123"
oo=""
for eer in kee:
    if eer.isalpha():
        oo+=eer
print(oo)
res=oo[::-1]
print(res)

class Animal():
    def monkey(self):
        print("Kia mia")
class human(Animal):
    def donkey(self):
        print("mia kia")

kkk=human()
kkk.monkey()
kkk.donkey()

sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for ii in sample_data:
    if ii!=():
        print(ii)
    if isinstance(ii,tuple):
        if len(ii)>0:
            print(ii)
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
#Largest number in nested array
nested=[[1,2,3,4],[5,6,7,8]]
neap=0
for x in nested:
    for y in x:
        if int(y)>neap:
            neap=int(y)
print(neap)
#all char sep
spe="Keerthi@123#vasan"
al=""
dif=""
alp=""
for x in spe:
    if x.isalpha():
        al+=x
    elif x.isdigit():
        dif+=x
    else:
        alp+=x
print(al)
print(dif)
print(alp)
nio=al+ dif+ alp
dii={}
"""if al in dii:
    dii[al]+=1
else:
    dii[al]=1
if dif in dii:
    dii[dif]+=1
else:
    dii[dif]=1
if alp in dii:
    dii[alp]+=1
else:
    dii[alp]=1
"""
for nio_s in nio:
    if nio_s in dii:
        dii[nio_s]+=1
    else:
        dii[nio_s]=1
print(dii)

        
