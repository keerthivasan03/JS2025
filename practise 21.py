multipl=9
for x in range(1,multipl+1):
    res=multipl*x
    print(multipl,"X", x, "=", res)
sum_of_even=0
for x in range(1,11):
    if x%2==0:
        print(x,"even")
        sum_of_even+=x
print(sum_of_even)
rever="121"
re=""
for x in rever:
    re=x+re
print(re)
rewo="Never odd or even"
rewo1=""
rewo2=""
for x in rewo:
    if x!=" ":    
        rewo1=x.lower()+rewo1
        rewo2=rewo2+x.lower()
print(rewo1, rewo2)
if(rewo2==rewo1):
    print("rewon")
else:
    print("notrewon")
years=["jan 2023","Jan 2024"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
        new=year.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)
name=["Keerthi vasan","Harishwadha siva"]
updated_name=[]
for namess in name:
    names=namess.lower()
    if names.startswith("harishwadha"):
        new_up=names.replace("harishwadha", "Anu")
        updated_name.append(new_up)
    else:
        updated_name.append(names)
print(updated_name)
middle_replace=["Keerthivasan is a goof"]
mid_up=[midu.replace("is","was") if midu.startswith("is",13) else midu for midu in middle_replace]
print(mid_up)
mm=["Kerthivasan is good"]
for midu_rev in mm:
    nn=[midu_rev[:12]+"si"+ midu_rev[14:]]
    print(nn)
count=34234324
dd=0
while count>0:
    count=count//10
    dd+=1
print(dd)
for x in range(1,16):
    if x%3==0 and x%5==0:
        print("FCX")
    elif x%3==0:
        print("FDS")
    elif x%5==0:
        print("QWE")
    else:
        print("SQFE")

sum_prime=0
for x in range(1,11):
    num_prime=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            num_prime+=1
    if num_prime==2:
        print(y)
        sum_prime+=y
print(sum_prime)
ff=5
nn=1
for x in range(1,ff+1):
    nn*=x
print(nn)
pattern=8
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("x",end="")
    print()
ll="89889075646"
k=0
for l in ll:
    if int(l)>k:
        k=int(l)
print(k)
count_letter="5435435435"
count_dic={}
for cc in count_letter:
    if cc in count_dic:
        count_dic[cc]+=1
    else:
        count_dic[cc]=1
print(count_dic)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user,t in FileServer.items():
    time+=FileServer[user]
print(round(time,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
list=[]
for first,last in list_full_names.items():
    for lasts in last:
        namm=first+" "+lasts
        list.append(namm)
        print(namm)
print(list)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
in_dic={}
for hard,ide in invert_resource_dict.items():
    for ides in ide:
        if ides in in_dic:
            in_dic[ides].append(hard)
        else:
            in_dic[ides]=[hard]
print(in_dic)
word_place="Jacki sherrif was a great 1989"
word=""
num=""
word_s=word_place.split()
for words in word_s:
    if words.isalpha():
        word+=words+" "
    else:
        num+=words+" "
word=word.strip()
num=num.strip()
print("{} in the period {}".format(word,num))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
ne=""
for d,na in network.items():
    ne+="{} have the id {}".format(d,na)+"\n"
print(ne)
wfc="apple banana apple orange banana apple kiravani"
wfc_d={}
wfcs=wfc.split()
for wfci in wfcs:
    if wfci in wfc_d:
        wfc_d[wfci]+=1
    else:
        wfc_d[wfci]=1
print(wfc_d)
sd={}
for x in range(1,11):
    c=x*x 
    sd[x]=c 
print(sd)   
id={"a": 1, "b": 2, "c": 3} 
idd={}
for a,b in id.items():
    idd[b]=a
print(idd) 
fd={"a": 5, "b": 15, "c": 8, "d": 20} 
fdd={}
for a,b in fd.items():
    if b>5:
        fdd[a]=b
print(fdd)
gfl=["apple", "banana", "apricot", "blueberry", "cherry","dragon"]
gfl_d={}
for g in gfl:
    firstl=g[0]
    if firstl not in gfl_d:
        gfl_d[firstl]=[]
    gfl_d[firstl].append(g)
print(gfl_d)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
list_com={name: detail for name,detail in zip(names, details)}
print(list_com)
word_letter="hello world"
wld={}
for ww in word_letter:
    if ww!=" ":    
        if ww in wld:
            wld[ww]+=1
        else:
            wld[ww]=1
print(wld)
merge1={"a": 10, "b": 20}
merge2={"b": 5, "c": 15}
merge1_copy=merge1.copy()
for aa,bb in merge2.items():
    if aa in merge1_copy:
        merge1_copy[aa]+=bb
    else:
        merge1_copy[aa]=bb
print(merge1_copy)
oo={num: "even" if num%2==0 else  "odd" for num in range(1,11)}
print(oo)
re=["python", "java", "c++"]
kk=[ki[::-1] for ki in re]
print(kk)
red={}
for kkk in re:
    rel=len(kkk)
    red[kkk]=rel
print(red)
fla={"a": [1, 2], "b": [3, 4], "c": [5]}
ss=set()
for aa,bb in fla.items():
    ss.update(bb)
print(ss)
comm1=[1, 2, 3, 4] 
comm2=[3, 4, 5, 6]
comm=[]
for com in comm1:
    if com in comm2:
        comm.append(com)
print(comm)
listing=[[1, 2], [3, 4], [5, 6]] 
lll=[]
for k in listing:
    for ki in k:
        lll.append(ki)
print(lll)
kkk=[5, 15, 25, 35, 45,11]
for kk in kkk:
    if kk%5==0:
        kki=kk+10
        print(kki)
