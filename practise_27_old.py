#multiplication
to_be=9
for x in range(1,to_be+1):
    multip_result=to_be*x
    print(to_be, "X", x, "=", multip_result)
#sum
sum_even=0
for x in range(1,11):
    if x%2==0:
        print(x, "= Even number")
        sum_even+=x
print(sum_even)
#reverse a number
rever_number="123"
rever_Store=""
for x in rever_number:
    rever_Store=x+rever_Store
print(rever_Store)
#count digits
to_be_count=5435345435
calc=0
while to_be_count>0:
    to_be_count=to_be_count//10
    calc+=1
print(calc)
#elif
for x in range(1,16):
    if x%3==0 and x%5==0:
        print(x, "Both")
    elif x%3==0:
        print(x, "3")
    elif x%5==0:
        print(x, "5")
    else:
        print(x, "Nothing")
#factorial
factorial_number=5
to_start=1
for x in range(1, factorial_number+1):
    to_start*=x
    print(to_start) # to check each iteration
print(to_start)
#pattern writing
pattern=5
for x in range(1,pattern+1):
    for y in range(1, x+1):
        print("X", end="")
    print()
#palindrome_check
palindrome_number="121121"
palindrome_store=""
for x in palindrome_number:
    palindrome_store=x+palindrome_store
print(palindrome_store)
if palindrome_store==palindrome_number:
    print(palindrome_number, "is Palindrome")
else:
    print(palindrome_number, "Not a Palindrome number")
#Palindrome_word
palindrome_word="Never odd Or even"
palindrome_store1=""
palindrome_store2=""
for x in palindrome_word:
    if x!=" ":
        palindrome_store1=x.lower()+palindrome_store1
        palindrome_store2=palindrome_store2+x.lower()
print(palindrome_store2, palindrome_store1)
if palindrome_store1==palindrome_store2:
    print(palindrome_word, "Is palindrome")
else:
    print(palindrome_word, "Not a Palindrome")
#largest digit
find_large="98437584395"
begin=0
for x in find_large:
    if int(x)>begin:
        begin=int(x)
print(begin)
#prime
prioe_end=0
for x in range(1,11):
    sio=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            sio+=1
    if sio==2:
            print(y)
            prioe_end+=y
print(prioe_end)
#replace
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for x in years:
    if x.endswith("2023"):
        new=x.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(x)
print(updated_years)
updati_years=[year.replace("2023","2025") if year.endswith("2023") else year for year in years]
print(updati_years)
#count_letter
count_letter="5435435435"
final_count={}
for x in count_letter:
    if x in final_count:
        final_count[x]+=1
    else:
        final_count[x]=1
print(final_count)
#adding values in key
FileServer = {"EndUser1": 2.25432, "EndUser2": 4.5324, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8} 
totals=0.0 
for key,value in FileServer.items():
    totals+=value
print(round(totals,2)) 
#appending in list
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
updated_name=[]
for first,last in list_full_names.items():
    for lasts in last:
        fine=first+" "+lasts
        updated_name.append(fine)
print(updated_name)
#append in dictionary
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs", "check"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards", "Check"]}
invert_resource={}
for key,value in invert_resource_dict.items():
    for values in value:
        values=values.lower()
        key=key.lower()
        if values in invert_resource:
            invert_resource[values]+=[key]
        else:
            invert_resource[values]=[key]
print(invert_resource)
#update in middle
word_place="Jacki sherrif was a great 1989"
word=""
number=""
word_place=word_place.split()
for x in word_place:
    print(x)
    if x.isalpha():
        word+=x+" "
    else:
        number+=x+" "
word=word.strip()
number=number.strip()
print("{} is the great man {}".format(word,number))
#update it with word in dic
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
finals=""
for key,value in network.items():
    finals+="{} have the id {}".format(key, value) +"\n"
print(finals)
#List
square_check=[ x*x for x in range(1,11)]
print(square_check)
even_number=[x for x in range(1,11) if x %2==0]
print(even_number)
conditional=["even" if x%2==0 else "odd" for x in range(1,11)]
print(conditional)
flist = [[1, 2], [3, 4], [5, 6]] 
nlist=[]
for x in flist:
    for y in x:
        nlist.append(y)
print(nlist)
nnlist=[y for x in flist for y in x]
print(nnlist)
clists1=[1, 2, 3, 4]
clists2=[3, 4, 5, 6]
finalss=[]
for k in clists1:
    if k in clists2:
        finalss.append(k)
print(finalss)
fflist=[k for k in clists1 if k in clists2]
print(fflist)
listss=["hello", "world", "python"]
update_list=[pia[::-1] for pia in listss]
print(update_list)
ft=[5, 15, 25, 35, 45,78]
for x in ft:
    if x%5==0:
        y=x+10
        print(y)
#dictionary
word_based="apple banana apple orange banana apple"
word_based=word_based.split()
word_dic={}
for words in word_based:
    word_first=words[0]
    if word_first in word_dic:
        word_dic[word_first]+=[words]
    else:
        word_dic[word_first]=[words]
print(word_dic)
word_based1="apple banana apple orange banana apple"
word_based1=word_based1.split()
word_dic1={}
for words1 in word_based1:
    if words1 in word_dic1:
        word_dic1[words1]+=1
    else:
        word_dic1[words1]=1
print(word_dic1)
sq_dic={}
for x in range(1,11):
    res=x*x
    sq_dic[x]=res
print(sq_dic)
invv={"a": 1, "b": 2, "c": 3}
new_inv={}
for key,value in invv.items():
    new_inv[value]=key
print(new_inv)
gre={"a": 5, "b": 15, "c": 8, "d": 20}
gre_dic={}
for key,value in gre.items():
    if value>5:
        gre_dic[key]=value
print(gre_dic)
gf=["apple", "banana", "apricot", "blueberry", "cherry", "grapes"]
new_gf={}
for gfs in gf:
    gfw=gfs[0]
    if gfw in new_gf:
        new_gf[gfw]+=[gfs]
    else:
        new_gf[gfw]=[gfs]
print(new_gf)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nd_dic={name:detail for name,detail in zip(names,details)}
print(nd_dic)
chhh="kEerthivasan"
chhh=chhh.lower()
new_chhh={}
for chh in chhh:
    if chh!=" ":
        if chh in new_chhh:
            new_chhh[chh]+=1
        else:
            new_chhh[chh]=1
print(new_chhh)
#merge
kk={"a": 10, "b": 20}
vv={"b": 5, "c": 15}
kk1=kk.copy()
for key,value in vv.items():
    if key in kk1:
        kk1[key]+=value
    else:
        kk1[key]=value
print(kk1)
in1=["python", "java", "c++"]
in1_dic={}
for ins in in1:
    wor=len(ins)
    in1_dic[ins]=wor
print(in1_dic)
Input={"a": [1, 2], "b": [3, 4], "c": [5]}
inn=[]
for key,value in Input.items():
    inn.extend(value)
print(inn)
eo={}
for x in range(1,11):
    if x%2==0:
        eo[x]="even"
    else:
        eo[x]="odd"
print(eo)
reverse_particular_word="I am learning python"
word_to=reverse_particular_word[5:13]
word_save=""
for x in word_to:
    word_save=x+word_save
    reverse_update=(reverse_particular_word[:5]+word_save+reverse_particular_word[13:])
print(reverse_update)
wordss="Jackie scherif was a greart actor in 1989 till 1999"
finals=wordss[:36]+"his period"+wordss[36:46]+"now he is"+wordss[46:]
print(finals)
word_place1="Jacki sherrif was a great 1989 2000"
words_spliy=word_place1.split()
outputs=[]
for i,x in enumerate(words_spliy):
    outputs.append(x)
    if x.isdigit():
        if x=="1989":
            outputs.append("Narrow")
        elif x=="2000":
            outputs.append("was a great period")
outputs=" ".join(outputs)
print(outputs)
word_place2="Jacki sherrif was a great 1989 2000"
words_spliy1=word_place2.split()
outputs1=[]
for i,x in enumerate(words_spliy1):
    outputs1.append(x)
    if x.isalpha():
        if x=="Jacki":
            outputs1.append("Mohammed")
        elif x=="was":
            outputs1.append("was a great period")
    if x.isdigit():
        if x=="1989":
            outputs1.append("Mohammed")
        elif x=="2000":
            outputs1.append("was a great period")
outputs1=" ".join(outputs1)
print(outputs1)
#search
def linear_search(list,key):
    for i, items in enumerate(list):
        if items==key:
            return i
    return -1
def binary_search(list,key):
    original_list=list[:]
    list.sort()
    left=0
    leng=len(list)
    right=leng-1
    while left<=right:
        middle=(right+left)//2
        if list[middle]==key:
            return original_list.index(key)
        if list[middle]>key:
            right=middle-1
        if list[middle]<key:
            left=middle+1
    return -1
print(linear_search([2, 3, 4, 1, 5, 6, 7, 8, 9, 10], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10],11 ))
#practise
def liner(list_of_name,key):
    for i,x in enumerate(list_of_name):
        if x==key:
            return i
    return -1
def binar(list_of_name,key):
    original=list_of_name[:]
    list_of_names=sorted(list_of_name)
    left=0
    length=len(list_of_names)
    right=length-1
    while left<=right:
        middle=(left+right)//2
        if list_of_names[middle]==key:
            return original.index(key)
        elif list_of_names[middle]<key:
            left=middle+1
        else:
            right=middle-1
    return -1
list_of_name = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor","Keerthi"]
print(liner(list_of_name,"Terry"))
print(binar(list_of_name,"Cameron"))
print(binar(list_of_name,"Keerthi"))



    






