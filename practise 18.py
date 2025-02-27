multiplicaiton=8
for x in range(1,multiplicaiton+1):
    result=x*multiplicaiton
    print(x, "*", multiplicaiton, "=", result)
sum=0
for x in range(1,11):
    if x%2==0:
        print(x, "even")
        sum+=x
print(sum)
reverse_number="121"
reverse=""
for x in reverse_number:
    reverse=x+reverse
print(reverse)
count_digit=89345345
digit=0
while count_digit>0:
    count_digit=count_digit//10
    digit+=1
print(digit)
for x in range(1,16):
    if x%3==0 and x%5==0:
        print(x, "fdsf")
    elif x%3==0:
        print(x, "uiore")
    elif x%5==0:
        print(x, "bnbb")
    else:
        print(x, "cdsd")
sum=0
for x in range(1,11):
    po=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            po+=1
    if po==2:
        print(y)
        sum+=y
print(sum)
factorial=5
factorial_cal=1
for x in range(1,factorial+1):
    factorial_cal*=x
print(factorial_cal)
pattern=9
for x in range(1, pattern+1):
    for y in range(1, x+1):
        print("X", end="")
    print()
reverse_word="Never odd or even"
reverse1=""
reverse2=""
#reverse_word_split=reverse_word.split()
for x in reverse_word:
    if x!=" ":
        reverse2=x.lower()+reverse2
        reverse1=reverse1+x.lower()
print(reverse1)
print(reverse2)
if(reverse2==reverse1):
    print("Same")
else:
    print("Not same")
largest_digit="542954358"
digits=0
for x in largest_digit:
    if int(x)>digits:
        digits=int(x)
print(digits)
word_replace=["Jan 123", "Jan 456", "Feb 123"]
word_replace_list=[]
for x in word_replace:
    if x.endswith("123"):
        change=x.replace("123", "456")
        word_replace_list.append(change)
    else:
        word_replace_list.append(x)
print(word_replace_list)
word_replace_list_comp=[x.replace("Jan","Feb") if x.startswith("Jan") else x for x in word_replace]
print(word_replace_list_comp)
count_letter="5435435435"
count_letter_dic={}
for x in count_letter:
    if x in count_letter_dic:
        count_letter_dic[x]+=1
    else:
        count_letter_dic[x]=1
print(count_letter_dic)
FileServer = {"EndUser1": 2.253243, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user, times in FileServer.items():
    time+=FileServer[user]
print(round(time, 2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
list_full_names_list=[]
for first, last in list_full_names.items():
    for lasts in last:
        full= first+" "+lasts
        list_full_names_list.append(full)
    else:
        list_full_names_list.append(first)
print(list_full_names_list)
invert_resource={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert_resource_dict={}
for device, lists in invert_resource.items():
    for liss in lists:  
        if liss in invert_resource_dict:
            invert_resource_dict[liss].append(device)
        else:
            invert_resource_dict[liss]=[device]
print(invert_resource_dict)
word_place="Jacki sherrif was a great 1989"
name=""
number=""
word_place_split=word_place.split()
for x in word_place_split:
    if x.isalpha():
        name+=x+" "
    else:
        number+=x
name=name.strip()
print("{} at {}".format(name, number))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
strr=""
for d, n in network.items():
    strr+="{} have the id {}".format(d, n) + "\n"
print(strr)
word_frequecy= "apple banana apple orange banana apple"
word_frequecy_dic={}
word_frequecy_split=word_frequecy.split()
for x in word_frequecy_split:
    if x in word_frequecy_dic:
        word_frequecy_dic[x]+=1
    else:
        word_frequecy_dic[x]=1
print(word_frequecy_dic)
squ_dic={}
for x in range(1,11):
    res=x*x
    squ_dic[x]=res
print(squ_dic)
invert_dic={}
inv={"a": 1, "b": 2, "c": 3}
for a, b in inv.items():
    invert_dic[b]=a
print(invert_dic)
filter_dic={}
filter_input={"a": 5, "b": 15, "c": 8, "d": 20}
for a,b in filter_input.items():
    if b>5:
        filter_dic[a]=b
print(filter_dic)
group_first=["apple", "banana", "apricot", "blueberry", "cherry"]
group_first_dic={}
for x in group_first:
    group_last=x[0]
    if group_last not in group_first_dic:
        group_first_dic[group_last]=[]
    group_first_dic[group_last].append(x)       
print(group_first_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nested={name: detail for name, detail in zip(names, details)}
print(nested)
character_frequency="hello world"
character_frequency_dic={}
for x in character_frequency:
    if x!=" ":
        if x in character_frequency_dic:
            character_frequency_dic[x]+=1
        else:
            character_frequency_dic[x]=1
print(character_frequency_dic)
merge1={"a": 10, "b": 20}
merge2={"b": 5, "c": 15}
merge1_copy=merge1.copy()
for n,m in merge2.items():
    if n in merge1:
        merge1_copy[n]+=m
    else:
        merge1_copy[n]=m
print(merge1_copy)
num_dic={f"{num}:even" if num%2==0 else f"{num}:odd" for num in range(1,11)}
print(num_dic)
length= ["python", "java", "c++"]
le={}
for lengths in length:
    word_length=len(lengths)
    le[lengths]=word_length
print(le)
flat={"a": [1, 2], "b": [3, 4], "c": [5]}
flat_set=set()
flat_list=[]
for s,j in flat.items():
    flat_set.update(j)
    flat_list.extend(j)
print(flat_list)
print(flat_set)
word_middle=["Name is Keerthi"]
word_middle_dic=[]
for x in word_middle:
    if x.startswith("is", 5):
        nn=x.replace("is", "was")
        word_middle_dic.append(nn)
    else:
        word_middle_dic.append(x)
print(word_middle_dic)
sq_dic=[n*n for n in range(1,11)]
print(sq_dic)
ev_dic=[n for n in range(1,11) if n%2==0 ]
print(ev_dic)
co_dic=["even" if n%2==0 else "odd" for n in range(1,11)]
print(co_dic)
flatt=[[1, 2], [3, 4], [5, 6]]
flatt_list=[flatting for f2 in flatt for flatting in f2]
print(flatt_list)
flats=[]
for f3 in flatt:
    for flatss in f3:
        flats.append(flatss)
print(flats)
com1=[1, 2, 3, 4] 
com2=[3, 4, 5, 6]
com_list=[coms for coms in com1 if coms in com2]
print(com_list) 
com=[]
for com11 in com1:
    if com11 in com2:
        com.append(com11)
print(com)
rv= ["hello", "world", "python"]
lii=[jk[::-1] for jk in rv]
print(lii)
lll=[5, 15, 25, 35, 45,54]
lkl=[add+10  for add in lll if add%5==0]
print(lkl)
for kl in lll:
    if kl%5==0:
        hj= kl+10
        print(hj)
