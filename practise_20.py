multip=8
for x in range(1,multip+1):
    res=multip*x
    print(multip, "*", x, "=", res)
sum_of_even=0
for x in range(1,11):
    if x%2==0:
        print(x, "even")
        sum_of_even+=x
print(sum_of_even)
revers_a_number="12434"
reverse_string=""
for reverse_nujmber in revers_a_number:
    reverse_string=reverse_nujmber+reverse_string
print(reverse_string)
reverse_word="Keerthi vasan"
reverse_word_string=""
for revre in reverse_word:
    if revre!=" ":
        reverse_word_string=revre+reverse_word_string
print(reverse_word_string)
reverse_palindrome="Never odd or even"
reverse_1=""
reverse_2=""
for reverese_palin in reverse_palindrome:
    if reverese_palin!=" ":    
        reverse_1=reverese_palin.lower()+reverse_1
        reverse_2=reverse_2+reverese_palin.lower()
print(reverse_1)
print(reverse_2)
if reverse_1==reverse_2:
    print("Palindrome")
else:
    print("Not a palindrome")
count_digit=65464543543
digit=0
while count_digit>0:
    count_digit=count_digit//10
    digit+=1
print(digit)
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x, "FizzBizz")
    elif x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Bizz")
    else:
        print(x, "Not a bizz")
sum_of_prime=0
for o in (1,11):
    count_prime=0
    for u in range(1,o+1):
        if u!=0 and o%u==0:
            count_prime+=1
    if count_prime==2:
            print(u)
            sum_of_prime+=u
print(sum_of_prime)
factorial=5
fact=1
for x in range(1,factorial+1):
    fact*=x
print(fact)
pattern=8
for x in range(1, pattern+1):
    for y in range(1, x+1):
        print("*", end="")
    print()
largest="54354398868"
largest_digit=0
for lar in largest:
    if int(lar)>largest_digit:
        largest_digit=int(lar)
print(largest_digit)
names=["Keerti vasan", "Anu vasan"]
final_name=[]
for name in names:
    if name.startswith("Keerti"):
        fill=name.replace("Keerti", "Hari")
        final_name.append(fill)
    else:
        final_name.append(name)
print(final_name)
year=["Jan 2023","Feb 2024","Jan 2024"]
updated=[years.replace("2024","2023") if years.endswith("2024") else years for years in year]
print(updated)
sums=0
for x in range(1,11):
    p=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            p+=1
    if p==2:
        print(y)
        sums+=y
print(sums)
count_letter="5435435435"
count_dic={}
for counts in count_letter:
    if counts in count_dic:
        count_dic[counts]+=1
    else:
        count_dic[counts]=1
print(count_dic)
FileServer = {"EndUser1": 2.255435, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user,tim in FileServer.items():
    time+=FileServer[user]
print(round(time,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
list_name=[]
for firs,las in list_full_names.items():
    for last in las:
        fulll=firs+" "+last
        list_name.append(fulll)
print(list_name)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert={}
for shop,address in invert_resource_dict.items():
    for addresss in address:    
        if addresss in invert:
            invert[addresss].append(shop)
        else:
            invert[addresss]=[shop]
print(invert)
word_place="Jacki sherrif was a great 1989"
namee=""
num=""
word_places=word_place.split()
for words in word_places:
    if words!=" ":
        if words.isalpha():
            namee+=words+" "
        else:
            num+=words
namee=namee.strip()
print("{} at {}".format(namee,num))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
networks=""
for do,id in network.items():
    networks+="{} is the {}".format(do, id)+"\n"
print(networks)
year_90=["1996","1997","1998","1999"]
year_20=["2003","2002","2001","2000"]
year_20.sort()
year_90.extend(year_20)
print(year_90)
word_f="apple banana apple orange banana apple"
word_spli=word_f.split()
words_dic={}
for wordd in word_spli:
    if wordd in words_dic:
        words_dic[wordd]+=1
    else:
        words_dic[wordd]=1
print(words_dic)
ii={}
for x in range(1,11):
    s=x*x
    ii[x]=s
print(ii)
invere={"a": 1, "b": 2, "c": 3}
new_invere={}
for aa, bb in invere.items():
    new_invere[bb]=aa
print(new_invere)
adding={"a": 5, "b": 15, "c": 8, "d": 20}
new_Adding={}
for cc,dd in adding.items():
    if dd>5:
        new_Adding[cc]=dd
print(new_Adding)
group_by=["apple", "banana", "apricot", "blueberry", "cherry"]
new_group_by={}
for grouby_by_letter in group_by:
    group_by_first=grouby_by_letter[0]
    if group_by_first not in new_group_by:
        new_group_by[group_by_first]=[]
    new_group_by[group_by_first]+=[grouby_by_letter]
print(new_group_by)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
name_detail={name:detail for name,detail in zip(names,details)}
print(name_detail)
character_f="hello world"
char_dic={}
for charac in character_f:
        if charac!=" ":
            if charac in char_dic:
                char_dic[charac]+=1
            else:
                char_dic[charac]=1
print(char_dic)
merge1={"a": 10, "b": 20}
merge2={"b": 5, "c": 15}
merge1_copy=merge1.copy()
for key,value in merge2.items():
    if key in merge1_copy:
        merge1_copy[key]+=value
    else:
        merge1_copy[key]=value
print(merge1_copy)
odd_dic={x: "even" if x%2==0 else  "odd" for x in range(1,11)}
print(odd_dic)
word_len= ["python", "java", "c++"]
#word_spl=word_len.split()
wor_dic={}
for wor in word_len:
    worr=len(wor)
    wor_dic[wor]=worr
print(wor_dic)
ooo={"a": [1, 2], "b": [3, 4], "c": [5]}
koo=[]
poo=set()
for k,v in ooo.items():
    koo.extend(v)
    poo.update(v)
print(koo)
print(poo)
revv=["hello", "world", "python"]
revv_dic=[ki[::-1] for ki in revv]
print(revv_dic)
comm1=[1, 2, 3, 4] 
comm2=[3, 4, 5, 6]
comm=[]
for commm in comm1:
    if commm in comm2:
        comm.append(commm)
print(comm)
listing=[[1, 2], [3, 4], [5, 6]] 
lll=[]
for l1 in listing:
    for l2 in l1:
        lll.append(l2)
print(lll)
kkk=[5, 15, 25, 35, 45,11]
for jjj in kkk:
    if jjj%5==0:
        jjj=jjj+10
        print(jjj)
update=["Keerthivasan is a good boy"]
replaces=[]
for updates in update:
    if updates.startswith("is",13):
        hhh=updates.replace("is","was")
        replaces.append(hhh)
    else:
        replaces.append(updates) 
print(replaces)
eee=[]
for xxx in update:
    if xxx.startswith("is",13):
        xxx=xxx[:13]+"si"+xxx[15:]
        eee.append(xxx)
print(eee)
