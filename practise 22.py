#mulitplicaiton
multi=8
for x in range(1,multi+1):
    result=x*multi
    print(multi,"*",x, "=", result)
#sum of even numbers
even_numbers=0
for x in range(1,11):
    if x%2==0:
        print(x,"EVen nujmber")
        even_numbers+=x
print(even_numbers)
#reverse word
reverse_word="Never odd or even"
reverse_word1=""
reverse_word2=""
for x in reverse_word:
    if x!=" ":
        reverse_word1=reverse_word1+x.lower()
        reverse_word2=x.lower()+reverse_word2
print(reverse_word2,reverse_word1)
if reverse_word1==reverse_word2:
    print("Palindrome")
else:
    print("Not a Palindrome")
#Reverse number
Reverse_number="121"
Reverse_number1=""
for x in Reverse_number:
    Reverse_number1=x+Reverse_number1
print(Reverse_number1)
if Reverse_number==Reverse_number1:
    print("Palindrome number")
#reverse in list
reverse_list=["python","Learning"]
reverse_list_final=[reverse_list_final1[::-1] for reverse_list_final1 in reverse_list]
print(reverse_list_final)
#reverse particular word
reverse_p_word="Keerthivasan is a good boy"
reverse_p_word_final=reverse_p_word[:18]+"doog"+reverse_p_word[22:]
print(reverse_p_word_final)
#replace last word
reverse_last_word=["Jan 2023", "Jan 2024"]
reverse_last_word_storage=[]
for x in reverse_last_word:
    if x.endswith("2023"):
        updated_list=x.replace("2023","2024")
        reverse_last_word_storage.append(updated_list)
    else:
        reverse_last_word_storage.append(x)
print(reverse_last_word_storage)
#replace any word
reverse_any_word=["Keethivasan weds Harishwadha"]
updated_any_word=[]
for x in reverse_any_word:
    x_lower=x.lower()
    if x_lower.startswith("weds",12):
        replace_word=x_lower.replace("weds","loves")
        updated_any_word.append(replace_word)
    else:
        updated_any_word.append(x_lower)
print(updated_any_word)
#count letters
count_letter=5435345435
counts=0
while count_letter>0:
    count_letter=count_letter//10
    counts+=1
print(counts)
#count words
count_words="Hello world"
count_letter="5435435435"
count_words_Store={}
#count_word_split=count_words.split()
for x in count_words:
   if x!=" ": 
    #print(x)
    if x in count_words_Store:
        count_words_Store[x]+=1
    else:
        count_words_Store[x]=1
print(count_words_Store)
#Fizzbizz
for x in range(1,15):
    if x%3==0 and x%5==0:
        print(x,"Fizz")
    elif x%3==0:
        print(x,"Bizz")
    elif x%5==0:
        print(x,"Fizz Bizz")
    else:
        print(x,"Not a Fizz Bizz")
#prime number count
p_count=0
for x in range(0,11):
    pr=0
    for y in range(0,x+1):
        if y!=0 and x%y==0:
            pr+=1
    if pr==2:
            print(y)
            p_count+=y
print(p_count)
#Factorial
factorial=5
factorial_multi=1
for x in range(1,factorial+1):
    factorial_multi*=x
print(factorial_multi)
#pattern
pattern=5
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("X", end="")
    print()
#largest digit
largest="43149090"
large=0
for x in largest:
    if int(x)>large:
        large=int(x)
print(large)
#list replace
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[year.replace("2023","2025") if year.endswith("2023") else year for year in years]
print(updated_years)
#count_letter
count_letter="5435435435"
count_letter_dic={}
for x in count_letter:
    if x in count_letter_dic:
        count_letter_dic[x]+=1
    else:
        count_letter_dic[x]=1
print(count_letter_dic)
FileServer = {"EndUser1": 2.25432, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0
for end,ti in FileServer.items():
    time+=FileServer[end]
print(time)
#append_names
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
list_full_list=[]
for first,last in list_full_names.items():
    for lasts in last:
        updated_name_list=first+" "+lasts
        list_full_list.append(updated_name_list)
print(list_full_list)
#swap name
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert_dict={}
for hard,ide in invert_resource_dict.items():
    for ides in ide:
        if ides in invert_dict:
            invert_dict[ides]+=[hard]
        else:
            invert_dict[ides]=[hard]
print(invert_dict)
#add names
word_place="Jacki sherrif was a great 1989"
alpha=""
numer=""
word_place_updated=[]
word_place_split=word_place.split()
for x in word_place_split:
    if x.isalpha():
        alpha+=x+" "
    else:
        numer+=x
alpha=alpha.strip()
print("{} at {}".format(alpha,numer))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
network_update=""
for domain, number in network.items():
    network_update+="{} is the id {}".format(domain,number)+"\n"
print(network_update)
#square
square_list=[]
for x in range(1,11):
    k=x*x
    square_list.append(k)
print(square_list)
#even_numbers
even=[]
for x in range(1,21):
    if x%2==0:
        even.append(x)
print(even)
#Conditional List
condition=["even" if x%2==0 else "odd" for x in range(1,11)]
print(condition)
even_odd_list=[]
for x in range(1,11):
    if x%2==0:
        even_odd_list.append("even")
    else:
        even_odd_list.append("Odd")
print(even_odd_list)
Nest=[[1, 2], [3, 4], [5, 6]] 
Next_final=[]
for kia in Nest:
    for kias in kia:
        Next_final.append(kias)
print(Next_final)
comm1=[1, 2, 3, 4] 
comm2=[3, 4, 5, 6]
comma=[]
for comm in comm1:
    if comm in comm2:
        comma.append(comm)
print(comma)
Fill=[5, 15, 25, 35, 45]
fia=[]
for x in Fill:
    if x%5==0:
       kk= x+10
       print(kk)
       fia.append(kk)
print(fia)
word_fre="apple banana apple orange banana apple"
word_Dic={}
word_spl=word_fre.split()
for x in word_spl:        
    if x in word_Dic:
        word_Dic[x]+=1
    else:
        word_Dic[x]=1
print(word_Dic)
Filters={"a": 5, "b": 15, "c": 8, "d": 20}
fil_dic={}
for val,key in Filters.items():
    if key>5:
        fil_dic[val]=key
print(fil_dic)
based_first=["apple", "banana", "apricot", "blueberry", "cherry","Kiapazham"]
first_dic={}
for x in based_first:
    based=x[0]
    if based not in first_dic:
        first_dic[based]=[x]
    else:
        first_dic[based]+=[x]
print(first_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
name_details={name: detail for name, detail in zip(names,details)}
print(name_details)
merg1={"a": 10, "b": 20}
merg2={"b": 5, "c": 15}
mer1_cop=merg1.copy()
for key,value in merg2.items():
    if key in mer1_cop:
        mer1_cop[key]+=value
    else:
        mer1_cop[key]=value
print(mer1_cop)
combine={num:"even" if num%2==0 else "odd" for num in range(1,11)}
print(combine)
final_leght= ["python", "java", "c++"]
length_dic={}
for x in final_leght:
    #final_leght=length.split()
    ll=len(x)
    length_dic[x]=ll
print(length_dic)
flatt={"a": [1, 2], "b": [3, 4], "c": [5]}
flat_dic=set()
for aa,bb in flatt.items():
    flat_dic.update(bb)
print(flat_dic)