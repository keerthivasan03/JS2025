#multiply program
multiplied_with=8
for x in range(1,multiplied_with+1):
    fanal=multiplied_with*x
    print(multiplied_with, "x", x, "=", fanal)
#sum of even
sum_of_even=0
for x in range(1,11):
    if x%2==0:
        print(x,"Even number")
        sum_of_even+=x
print(sum_of_even)
#reverse a number
reverse_number="4123213"
reverse_store=""
for x in reverse_number:
    reverse_store=x+reverse_store
print(reverse_store)
#count digits
count_digit=5435345345234
digit=0
while count_digit>0:
    count_digit=count_digit//10
    digit+=1
print(digit)
#fizzBuzz
for x in range(1,16):
    if x%3==0 and x%5==0:
        print(x, "FIZZBIZZ")
    elif x%3==0:
        print(x,"FIZZ")
    elif x%5==0:
        print(x, "BUZZ")
    else:
        print(x,"No FIZZZZZ")
#prime numner
prame=0
for x in range(1,11):
    x_cal=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            x_cal+=1
    if x_cal==2:
        print(y,"Prime number")
        prame+=y
print(prame)
#factorial number
factorial=5
fact_mul=1
for x in range(1,factorial+1):
    fact_mul*=x
print(fact_mul)
#pattern
pattern=8
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("x",end="")
    print()
#palindrom number check
palindrome="4324234"
palindrome_num=""
for x in palindrome:
    palindrome_num=x+palindrome_num
print(palindrome_num)
if (palindrome_num==palindrome):
    print(palindrome, "Is a palindrome")
else:
    print(palindrome,"Not palindrome")
#largest digit
largest_digit="54234234598"
starting=0
for x in largest_digit:
    if int(x)>starting:
        starting=int(x)
print(starting)
#replace
Years= ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[] #creating list
for x in Years:
    if x.endswith("2023"):
        update=x.replace("2023","2025")
        updated_years.append(update)
    else:
        updated_years.append(x)
print(updated_years)
#replace in list comprehension
Years= ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years1=[year.replace("2023","2025") if year.endswith("2023") else year for year in Years]
print(updated_years1)
#count letter
count_letter="5435435435"
count_dic={} #creating dic to chec
for x in count_letter:
    if x in count_dic:
        count_dic[x]+=1
    else:
        count_dic[x]=1
print(count_dic)
#adding the integer
FileServer = {"EndUser1": 2.2578934, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for end,number in FileServer.items():
    time+=number #iterate number in dictionary
print(round(time,2))
#appending the names with dictionary
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
final_list=[]
for first,last in list_full_names.items():#separating key and value
    for lasts in last: #iterating the value in dict
        full_name=first+" "+lasts #appending the values
        final_list.append(full_name)
print(final_list)
#key to value value to key
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert_resource_dict_new={}
for parts,hards in invert_resource_dict.items():
    for hard in hards:    
        if hard in invert_resource_dict_new:
            invert_resource_dict_new[hard]+=[parts]
        else:
            invert_resource_dict_new[hard]=[parts]
print(invert_resource_dict_new)
#adding words in middle
word_places="Jacki sherrif was a great 1989 at this period"
alpha=""
beta=""
word_place=word_places.split()
for x in word_place:
    if x.isalpha():
        alpha+=x+" "
    else:
        beta=x
alpha=alpha.strip()
print("{} in the year {}".format(alpha, beta))
# in middle wherever we want
word_places = "Jacki sherrif was a great 1989 at this period"
alpha = ""
beta = ""

word_place = word_places.split()
found_number = False  # To mark when we find the first non-alphabetic word

for x in word_place:
    if x.isalpha():
        if not found_number:
            alpha += x + " "  # Add to alpha until we find a number
        else:
            beta += x + " "  # Everything after the first number goes to beta
    else:
        if not found_number:
            beta += x + " "  # Store the first number in beta
            found_number = True
        else:
            beta += x + " "  # Append the rest of the sentence to beta

alpha = alpha.strip()
beta = beta.strip()

print("{} in the year {}".format(alpha, beta))
#combine it with dictionary
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
new_store=""
for domain,number in network.items():
    new_store+="{} is the {}".format(domain,number)+"\n"
    print(new_store)
#list comprehension square
square=[x for x in range(1,11) if x%2==0]
print(square)
even=[x*x for x in range(1,11)]
print(even)
condi=["even" if x%2==0 else "odd" for x in range(1,11)]
print(condi)
neste=[[1, 2], [3, 4], [5, 6]]
new=[]
for nest in neste:
    for kia in nest:
        new.append(kia)
print(new)
com1=[1, 2, 3, 4]
com2=[3, 4, 5, 6]
com3=[]
for com in com2:
    if com in com1:
        com3.append(com)
print(com3)
rev=["hello", "world", "python"]
lis=[mia[::-1] for mia in rev]
print(lis)
oo=[5, 15, 25, 35, 45,78]
for ki in oo:
    if ki%5==0:
        add=ki+10
        print(add)
#word dic
frut="apple banana apple orange banana apple"
fruit1={}
fruit=frut.split()
for fruits in fruit:
    if fruits in fruit1:
        fruit1[fruits]+=1
    else:
        fruit1[fruits]=1
print(fruit1)
sp={}
for x in range(1,11):
    rr=x*x
    sp[x]=rr
print(sp)
invert={"a": 1, "b": 2, "c": 3}
invert_dic={}
for a,b in invert.items():
    invert_dic[b]=a
print(invert_dic)
fil_dic= {"a": 5, "b": 15, "c": 8, "d": 20}
fil_final={}
for a,b in fil_dic.items():
    if b>5:
        fil_final[a]=b
print(fil_final)
kk=["apple", "banana", "apricot", "blueberry", "cherry"]
kk_dic={}
for kii in kk:
    kiii=kii[0]
    if kiii in kk_dic:
        kk_dic[kiii]+=[kii]
    else:
        kk_dic[kiii]=[kii]
print(kk_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
fii={name: detail for name,detail in zip(names,details)}
print(fii)
io= "hello world"
kio={}
for ios in io:
    if ios!=" ":    
        if ios in kio:
            kio[ios]+=1
        else:
            kio[ios]=1
print(kio)
copy1= {"a": 10, "b": 20}
copy2= {"b": 5, "c": 15}
copy3=copy1.copy()
for key,value in copy2.items():
    if key in copy3:
        copy3[key]+=value
    else:
        copy3[key]=value
print(copy3)
in1=["python", "java", "c++"]
in2={}
for in3 in in1:
    lens=len(in3)
    in2[in3]=lens
print(in2)
flatten={"a": [1, 2], "b": [3, 4], "c": [5]}
dic=[]
for a,b in flatten.items():
    dic.extend(b)
print(dic)
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

reverse_particular_word="I am learning python"
word_to_reverse=reverse_particular_word[5:13]
word_save=""
for x in word_to_reverse:
    word_save=x+word_save
reverse_update=(reverse_particular_word[:5]+word_save+reverse_particular_word[13:])
print(reverse_update)