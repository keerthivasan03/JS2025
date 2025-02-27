multiplication=7
for multi in range(1,11):
    result=multi*multiplication
    print(multi,"X", multiplication, "=", result)
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
if(reverse==reverse_number):
    print("palindrome")
else:
    print("No p")
count_digits=435435
digit_count=0
while count_digits>0:
    count_digits=count_digits//10
    digit_count+=1
print(digit_count)
for x in range(1,10):
    if x%3==0 and x%5==0:
        print(x, "fizzbizz")
    elif x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Bizz")
    else:
        print(x, "No FizzBizz")
sums=0
for x in range(1,11):
    incre=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            incre+=1
    if incre==2:
            print(y)
            sums+=y
print(sums)
factorial_number=7
factorial_mul=1
for factorial in range(1, factorial_number+1):
    factorial_mul*=factorial
print(factorial_mul)
pattern=9
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("*", end="")
    print()
reverse_word="Never odd or even"
reverse_word1=""
reverse_word2=""
for iteration in reverse_word:
    if iteration!=" ":
        reverse_word1=iteration.lower()+reverse_word1
        reverse_word2=reverse_word2+iteration.lower()
print(reverse_word1, reverse_word2)
if(reverse_word2==reverse_word1):
    print("Palin")
else:
    print("no palin")
largest_digit="5435467"
lowest=0
for x in largest_digit:
    if int(x)>lowest:
        lowest=int(x)
print(lowest)
namess=["keerthi vasan"]
name_list=[]
for name in namess:
 if name.endswith("vasan"):
    names=name.replace("vasan", "keerhti")
    name_list.append(names)
 else:
    name_list.append(name)
print(name_list)
name_list_comp=[name.replace("keerthi", "keerthiiiiiiiiiiiiiiii") if name.startswith("keerthi") else name for name in namess]
print(name_list_comp)
count_letter="793749873982432"
count_letter_list={}
for couns in count_letter:
    if couns not in count_letter_list:
        count_letter_list[couns]=1
    else:
        count_letter_list[couns]+=1
print(count_letter_list)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user, value in FileServer.items():
    time+=FileServer[user]
print(round(time,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
final_list=[]
for first, last in list_full_names.items():
    for lasts in last:
        name_concat=first+" "+lasts
        final_list.append(name_concat)
print(final_list)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert={}
for shop, details in invert_resource_dict.items():
    for detail in details:
        if detail in invert:
            invert[detail]+=[shop]
        else:
            invert[detail]=[shop]
print(invert)
word_plac="Jacki sherrif was a great 1989"
alpha=""
beta=""
word_place=word_plac.split()
for word_places in word_place:
    #if word_place!=" ":
     if word_places.isalpha():
        alpha+=word_places+" "
     else:
        beta+=word_places
alpha=alpha.strip()
print("{} in the period {}".format(alpha, beta))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
empty=""
for name, details in network.items():
    empty+="{} is the id {}".format(name, details) + "\n"
print(empty)
word_fre="apple banana apple orange banana apple"
word_split=word_fre.split()
word_free={}
for words in word_split:
    if words in word_free:
        word_free[words]+=1
    else:
        word_free[words]=1
print(word_free)
sq={}
for x in range(1,11):
    q=x*x
    sq[x]=q
print(sq)
invert_dic={"a": 1, "b": 2, "c": 3}
dic_inv={}
for value, key in invert_dic.items():
    dic_inv[key]=value
print(dic_inv)
fil_dic={"a": 5, "b": 15, "c": 8, "d": 20}
dic_fil={}
for key, value in fil_dic.items():
    if value>5:
        dic_fil[key]=value
print(dic_fil)
group_firs="apple banana aukfruit orange banyan apricot custard "
group_dic={}
group_first=group_firs.split()
for groups in group_first:
    grouping=groups[0]
    if grouping in group_dic:
        group_dic[grouping].append(groups)
    else:
        group_dic[grouping]=[groups]
print(group_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
name_com={name: detail for name, detail in zip(names, details)}
print(name_com)
character_fre="Keerthi vasSan"
character_lower=character_fre.lower()
char_dic={}
for character in character_lower:
    if character!=" ":
        if character in char_dic:
            char_dic[character]+=1
        else:
            char_dic[character]=1
print(char_dic)
merge1={"a": 10, "b": 20}
merge2={"b": 5, "c": 15}
merge1_copy=merge1.copy()
for key, val in merge2.items():
    if key in merge1_copy:
        merge1_copy[key]+=val
    else:
        merge1_copy[key]=val
print(merge1_copy)
odd_even={num: "even" if num%2==0 else "odd" for num in range(1,11)}
print(odd_even)
Inputs= ["python", "java", "c++"]
nones={}
#Inputs=Input.split(",")
input_length=len(Inputs)
for ins in Inputs:
    nones[ins]=len(ins)
print(nones)
mergeing={"a": [1, 2], "b": [3, 4], "c": [5]}
saved=[]
for key, value in mergeing.items():
    saved.extend(value)
print(saved)
squ=[n*n for n in range(1,11)]
print(squ)
eve=[n for n in range(1,11) if n%2==0]
print(eve)
od=[f"{num:}  even" if num%2==0 else f"{num:} odd" for num in range(1,11)]
print(od)
flatt=[[1, 2], [3, 4], [5, 6]] 
flat=[]
for nn in flatt:
    for no in nn:
        flat.append(no)
print(flat)
list1=[1, 2, 3, 4]
list2=[3, 4, 5, 6]
listt=[]
for lists in list1:
    if lists in list2:
        listt.append(lists)
print(listt)
revv=["hello", "world", "python"]
comp=[kia[::-1] for kia in revv]
print(comp)
fil=[5, 15, 25, 35, 45]
ff=[add+10 for add in fil if add%5==0]
print(ff)


