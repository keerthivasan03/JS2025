def multi(n):
    for x in range(1,n+1):
        result=x*n
        print(x,"x",n,"=", result)
multi(8)
sum=0
for x in range(1,11):
    if x%2==0:
        print(x)
        sum+=x
print(sum)
reverse_number="8945"
reverse_store=""
for x in reverse_number:
    reverse_store=x+reverse_store
print(reverse_store)
count_digits=89432
c=0
while count_digits>0:
    count_digits=count_digits//10
    c+=1
print(c)
for x in range(1,11):
    if x%3==0:
        print(x, "f")
    elif x%5==0:
        print(x, "B")
    elif x%5==0 and x%3==0:
        print(x, "FB")
    else:
        print(x, "FBN")
s=0
for x in range(1,11):
    p=0
    for y in range(1,x+1):
        if x%y==0 and y!=0:
            p+=1
    if p==2:
            print(y)
            s+=y
print(s)
def facr(n):
    f=1
    for x in range(1,n+1):
        f*=x
    print(f)
facr(5)
for x in range(1,8):
    for y in range(1,x+1):
        print("x", end="")
    print()
pali="Never odd or even"
res1=""
res2=""
for x in pali:
    if x!=" ":
        res1=x.lower() + res1
        res2=res2 + x.lower()
print(res2, res1)
larget="7843294"
n=0
for x in larget:
    if int(x)>n:
        n=int(x)
print(n)
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
up=[year.replace("2023","2024") if year.endswith("2023") else year for year in years]
print(up)
upda=[]
for year in years:
    if year.endswith("2024"):
        new=year.replace("2024","2025")
        upda.append(new)
    else:
        upda.append(year)
print(upda)
count_letter="5435435435"
count_dic={}
for x in count_letter:
    if x in count_dic:
        count_dic[x]+=1
    else:
        count_dic[x]=1
print(count_dic)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
tot=0.0
for key,value in FileServer.items():
    tot+=value
print(round(tot,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
kk=[]
for key,value in list_full_names.items():
    for values in value:
        upa=key+" "+values
        kk.append(upa)
print(kk)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
inv_dic={}
for key,value in invert_resource_dict.items():
    for values in value:
        if values in inv_dic:
            inv_dic[values]+=[key]
        else:
            inv_dic[values]=[key]
print(inv_dic)
word_place="Jacki sherrif was a great 1989"
num=""
alp=""
word_place=word_place.split()
for x in word_place:
    if x.isalpha():
        alp+=x+" "
    else:
        num+=x
alp=alp.strip()
print(f"{alp} was great {num}")
out=[]
for x in word_place:
    out.append(x)
    if x.isalpha():
        if x=="sherrif":
            out.append("mass maharaja")
        elif x=="is":
            out.append("dummy maharaja")
    elif x.isnumeric():
        if x=="1999":
            out.append("oooo")
        elif x=="1989":
            out.append("38942943")
outpu=" ".join(out)
print(outpu)
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
for key,value in network.items():
    print(f"{key} is {value}")
sq=[x*x for x in range(1,11)]
print(sq)
ee=[x for x in range(1,11) if x%2==0]
print(ee)
con={x:"even" if x%2==0 else "odd" for x in range(1,11)}
print(con)
fl=[[1, 2], [3, 4], [5, 6]] 
q=[]
for x in fl:
    for k in x:
        q.append(k)
print(q)
a=[1, 2, 3, 4] 
b=[3, 4, 5, 6]
for k in a :
    if k in b:
        print(k)

re=["hello", "world", "python"]
re_d={}
for x in re:
    ll=len(x)
    re_d[x]=ll
    print(x[::-1])
print(re_d)
re_l=[rr[::-1] for rr in re]
print(re_l)
nl=[5, 15, 25, 35, 45,44]
for n in nl:
    if n%5==0:
        k=n+10
        print(k)
ww="apple banana apple orange banana apple"
ww_dic={}
ww=ww.split()
for x in ww:
    if x in ww_dic:
        ww_dic[x]+=1
    else:
        ww_dic[x]=1
print(ww_dic)
nnn={}
for x in range(1,11):
    nn=x*x
    nnn[x]=nn
print(nnn)
i={"a": 1, "b": 2, "c": 3}
io={}
for key,value in i.items():
    io[value]=key
print(io)
o={"a": 5, "b": 15, "c": 8, "d": 20}
no={}
for key,value in o.items():
    if value>5:
        no[key]=value
print(no)
gb=["apple", "banana", "apricot", "blueberry", "cherry"]
gb_d={}
for x in gb:
    bb=x[0]
    if bb in gb_d:
        gb_d[bb]+=[x]
    else:
        gb_d[bb]=[x]
print(gb_d)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
update_name={name:detail for name,detail in zip(names,details)}
print(update_name)
ch_fr="hello world"
ch_dic={}
for x in ch_fr:
    if x!=" ":
        if x.lower() in ch_dic:
            ch_dic[x]+=1
        else:
            ch_dic[x]=1
print(ch_dic)
import copy
a={"a": 10, "b": 20}
b={"b": 5, "c": 15}
n=copy.deepcopy(a)
for ky,value in b.items():
    if ky in n:
        n[ky]+=value
    else:
        n[ky]=value
print(n)
m={"a": [1, 2], "b": [3, 4], "c": [5]}
d=[]
for key,value in m.items():
    d.extend(value)
print(d)
li_di1=[[1, 2], [3, 4], [5, 6]] 
n_l=[]
for x in li_di1:
    if isinstance(x,list):
        n_l.extend(x)
    else:
        n_l.append(x)
print(n_l)
li_2=[1, [2, [3, 4]], 5]
nn_l=[]
def flatten(li):
    for x in li:
        if isinstance(x,list):
            flatten(x)
        else:
            nn_l.append(x)
flatten(li_2)
print(nn_l)
name="Keerthi vasan"
vowel="aeiou"
name_lower=name.lower()
s=0
vo={}
for x in name_lower:
    if x in vowel:
        s+=1
        if x in vo:
            vo[x]+=1
        else:
            vo[x]=1
print(vo)
print(s)
