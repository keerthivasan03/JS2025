flatten_dictionary={"a": [1, 2], "b": [3, 4], "c": [5]}
storage_1=[]
for c,d in flatten_dictionary.items():
        storage_1.extend(d)
print(storage_1)
flatten_dictionary={"a": [1, 2], "b": [3, 4], "c": [6]}
storage_2=set()
for e,f in flatten_dictionary.items():
        storage_2.update(f)
print(storage_2)
word_length=["python", "java", "c++"]
storage_3={}
for word_lengths in word_length:
    word_length_store=len(word_lengths)
    storage_3[word_lengths]= word_length_store
print(storage_3)
even_odd=[f"{num:} even" if num%2==0 else f"{num}: odd" for num in range(1,11)]
print(even_odd)
input_a={"a": 10, "b": 20}
input_b={"b": 5, "c": 15}
final_output=input_a.copy()
for key1,value1 in input_b.items():
        if key1 in final_output:
            final_output[key1]+=value1
        else:
              final_output[key1]=value1
print(final_output)
character_frequency="keerthi vasan"
character_frequency_store={}
#character_frequency_split=character_frequency.split()
for character_frequency_split in character_frequency:
    if character_frequency_split!=" ":
        if character_frequency_split in character_frequency_store:
            character_frequency_store[character_frequency_split]+=1
        else:
            character_frequency_store[character_frequency_split]=1
print(character_frequency_store) 

names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
z={name: details for name, details in zip(names, details)}
print(z)
based_letter_order= ["apple", "banana", "apricot", "blueberry", "cherry"]
based_letter_order_store={}
for based_letter_order1 in based_letter_order:
    first_letter=based_letter_order1[0]
    if first_letter not in based_letter_order_store:
        based_letter_order_store[first_letter]=[]
    based_letter_order_store[first_letter].append(based_letter_order1)
print(based_letter_order_store)
filter_dictionary={"a": 5, "b": 15, "c": 8, "d": 20}
filter_dictionary_store={}
for key2, value2 in filter_dictionary.items():
    if value2>5:
         filter_dictionary_store[key2]=value2
    print(filter_dictionary_store)
inverted_dictionary={"a": 1, "b": 2, "c": 3}
inverted_dictionary_store={}
for key3,value3 in inverted_dictionary.items():
     inverted_dictionary_store[value3]=key3
print(inverted_dictionary_store)         
value_square=[f"{num}: {num*num}"  for num in range(1,6)]
print(value_square)
value_square = [f"{num}: {num * num}" for num in range(1, 6)]
print(value_square)
value_square_dictionary={}
for x in range(1,6):
    res=x*x
    value_square_dictionary[x]=res
print(value_square_dictionary)
input_fruits="apple banana apple orange banana apple"
assign_dictionary={}
input_fruits_split=input_fruits.split()
for input_split in input_fruits_split:
    if input_split in assign_dictionary:
        assign_dictionary[input_split]+=1
    else:
        assign_dictionary[input_split]=1
print(assign_dictionary)
fit=[5, 15, 25, 35, 45]
filter_transform=[fits+10 for fits in fit if fits%5==0]
print(filter_transform)
fit1=["hello", "world", "python"]
fit2=[fit3[::-1] for fit3 in fit1]
print(fit2)   
com1=[1, 2, 3, 4]
com2=[3, 4, 5, 6]    
com3=[ress for ress in com2 if ress in com1]
print(com3) 
cond=[f"{num}: {num*num}" for num in range(1,11)]
print(cond)
def network(poda):
    normal=""
    for key,value in poda.items():
        normal+="{} is the server name with id {}".format(key, value)+ "\n"
    return normal
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))
word_place="Jacki sherrif was a great 1989"
word_place_split=word_place.split()
name=""
year=""
for word in word_place_split:
    if word.isalpha():
        name+=word+" "
    else:
        year=word
name=name.strip()
print("{} for range of period {}".format(name, year))     
invert_resource_dict=({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]})
res_dic={}
for key,value in invert_resource_dict.items():
    for values in value:
        if values in res_dic:
            res_dic[values].append(key)
        else:
             res_dic[values]=[key] 
print(res_dic)  
list_full_names=({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]})
full_name=[]
for first, second in list_full_names.items():
     for last in second:
          full=first+" "+last
          full_name.append(full)
print(full_name)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for key, value in FileServer.items():
     time+=value
print(time)
count_letter="1231234"
count={}
for counting in count_letter:
    if counting in count:
         count[counting]+=1
    else:
         count[counting]=1    
print(count)
years_normal=["jan 2023", "dec 2023", "kee 2025"]
updated_years_normal=[]
for year_normal in years_normal:
    if year_normal.endswith("2023"):
        updated=year_normal.replace("2023","2025")
        updated_years_normal.append(updated)
    else:
        updated_years_normal.append(year_normal)
print(updated_years_normal)

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
       replp=year.replace("2023","2024")
       updated_years.append(replp)
    else:
        updated_years.append(year)
print(updated_years)
years = ["January 2025", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[year.replace("2023","2024") if year.endswith("2023") else year for year in years]
print(updated_years)
largest_digit="687668"
co=0
for x in largest_digit:
     if int(x)>co:
          co=int(x)
print(co)
palindrone="32132"
rev=""
for x in palindrone:
    rev=palindrone+rev
print(rev)
if rev==palindrone:
     print(palindrone)
else:
     print("None")
palin_word="Never odd or even"
rev1=""
rev2=""
for x in palin_word:
    if x!=" ":
        rev1=x.lower()+rev1
        rev2=rev2+x.lower()
print(rev1)
print(rev2)
if rev2==rev1:
     print(palin_word)
else:
     print("nne")
pattern=9
for x in range(1,pattern+1):
    for y in range(1, x+1):
          print("X", end="")
    print()
factor=120
res1=1
for x in range(1,factor+1):
     res1*=x
print(res1)

s=0
for x in range(1,10):
    pp=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            pp+=1
    if pp==2:
            print(y)
            s+=y
print(s)
for x in range(1,11):
    if x%3==0 and x%5==0:
          print("p")
    elif x%3==0:
         print("q")
    elif x%5==0:
         print("u")
    else:
         print("ioi")
cc=4324324
d=0
while cc>0:
    cc=cc//10
    d+=1
print(d)
sum=0
sumi=0
for x in range(1,11):
     if x%2==0:
        print(x)
        sum+=x
print(sum)
multi=9
for x in range(1,11):
     rrr=multi*x
     print(multi, "x", x,  "=", rrr)    


names=['keerthi', 'vasan', 'anu', 'harish', 'wadha']   
#sorted= names.sort    
print(sorted(names, key=len))