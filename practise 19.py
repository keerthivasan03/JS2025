ml=8
for x in range(1, ml+1):
    re=ml*x
    print(ml, "x", x, "=", re)
su=0
for x in range(1,11):
    if x%2==0:
        print(x, "even")
        su+=x
print(su)
rev="121"
rev1=""
for x in rev:
    rev1=x+rev1
print(rev1)
if rev1==rev:
    print("same")
else:
    print("jkfds")
cd=54354354
d=0
while cd>0:
    cd=cd//10
    d+=1
print(d)
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x, "jfdsf")
    elif x%3==0:
        print(x, "rewre")
    elif x%5==0:
        print(x, "fdsfd")
    else:
        print(x, "fhfjffj")
sum=0
for x in range(1,11):
    pn=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            pn+=1
    if pn==2:
        print(y)
        sum+=y
print(sum)
f=5
xx=1
for x in range(1,f+1):
    xx*=x
print(xx)
p=9
for x in range(1,p+1):
    for y in range(1,x+1):
        print("x", end="")
    print()
rev_wrd="Never odd or even"
rev_wrd1=""
rev_wrd2=""
for x in rev_wrd:
    if x!=" ":
        rev_wrd1=x.lower()+rev_wrd1
        rev_wrd2=rev_wrd2+x.lower()
print(rev_wrd1)
print(rev_wrd2)
if rev_wrd1==rev_wrd2:
    print("jdsljds")
else:
    print("fssd")
ld="4354354398"
li=0
for x in ld:
    if int(x)>li:
        li=int(x)
print(li)
name_update=["Keerthivasan is a good boy"]
updated_name=[]
for x in name_update:
    if x.startswith("is", 13):
        name=x.replace("is", "was")
        updated_name.append(name)
    else:
        updated_name.append(x)
print(updated_name)
updated_namm=[x.replace("is", "kia") if x.startswith("is", 13) else x for x in name_update]
print(updated_namm)
name_updte = ["Keerthivasan is a good boy"]
updatd = []
for x in name_updte:
    if x.startswith("is", 13):  # Check if "is" appears at index 13
        x = x[:13] + "si" + x[15:]  # Replace "is" with "si"
    updatd.append(x)
print(updatd)
count_letter="5435435435"
cl={}
for x in count_letter:
    if x in cl:
        cl[x]+=1
    else:
        cl[x]=1
print(cl)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user,times in FileServer.items():
    time+=FileServer[user]
print(round(time, 2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
lists=[]
for first,last in list_full_names.items():
    for lasts in last:
        new=first+" "+lasts
        lists.append(new)
print(lists)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert={}
for hard, ide in invert_resource_dict.items():
    for ides in ide:
        if ides in invert:
            invert[ides].append(hard)
        else:
            invert[ides]=[hard]
print(invert)
word_place="Jacki sherrif was a great 1989"
name=""
numer=""
word_place_split=word_place.split()
for words in word_place_split:
    if words.isalpha():
        name+=words+" "
    else:
        numer+=words
name=name.strip()
print("{} at {}".format(name, numer))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
net=""
for domain,nujmber in network.items():
    net+="{} is the number {}".format(domain,nujmber) + "\n"
print(net)
wf="apple banana apple orange banana apple"
wfd={}
wfs=wf.split()
for wfi in wfs:
    if wfi in wfd:
        wfd[wfi]+=1
    else:
        wfd[wfi]=1
print(wfd)
filters={"a": 5, "b": 15, "c": 8, "d": 20}
filterd={}
for aa,bb in filters.items():
    if bb>5:
        filterd[aa]=[bb]
print(filterd)
gr=["apple", "banana", "apricot", "blueberry", "cherry"]
group_dic={}
#grs=gr.split()
for froup in gr:
    group_first=froup[0]
    if group_first not in group_dic:
        group_dic[group_first]=[]
    group_dic[group_first].append(froup)
print(group_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
out={name:detail for name, detail in zip(names, details)}
print(out)
inp="hello world"
#ii=inp.split()
kin={}
for kia in inp:
    if kia!=" ":
        if kia in kin:
            kin[kia]+=1
        else:
            kin[kia]=1
print(kin)
merge1={"a": 10, "b": 20}
merge2= {"b": 5, "c": 15}
merge1_cop=merge1.copy()
for aa,bb in merge2.items():
    if aa in merge1_cop:
        merge1_cop[aa]+=bb
    else:
        merge1_cop[aa]=bb
print(merge1_cop)
odd_dic={}
for k in range(1,11):
    if k%2==0:
        odd_dic[k]="even"
    else:
        odd_dic[k]="odd"
print(odd_dic)
flatten={"a": [1, 2], "b": [3, 4], "c": [5]}
flah=set()
for bh,yu in flatten.items():
    flah.update(yu)
print(flah)
wordd=["python", "java", "c++"]
www={}
for weord in wordd:
    wordd_len=len(weord)
    www[weord]=wordd_len
print(www)
single_lisy=[[1, 2], [3, 4], [5, 6]] 
kkk=[]
for ko in single_lisy:
    for f2 in ko:
        kkk.append(f2)
print(kkk)
zx=[1, 2, 3, 4]
cv=[3, 4, 5, 6]
jk=[]
for kk in zx:
    if kk in cv:
        jk.append(kk)
print(jk)
bn=["hello", "world", "python"]
jj=[]
for bo in bn:
    jj.append(bo[::-1])
print(jj)
    
