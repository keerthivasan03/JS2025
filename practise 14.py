multiplication=7
for num in range(1,11):
    multiplication_result=num*multiplication
    print(multiplication_result)
sum_of_even_number=0
for num in range(1,11):
    if num%2==0:
        print(num, " Is the even number")
        sum_of_even_number+=num
print(sum_of_even_number)
reverse_number="54354353"
reverse_number_final=""
for num in reverse_number:
    reverse_number_final=num+reverse_number_final
print(reverse_number_final)
if reverse_number_final==reverse_number:
    print(reverse_number, " is palindrome number")
else:
    print(reverse_number, " is not a palindrome number")
reverse_word="Never odd or even"
reverse_word1=""
reverse_word2=""
for reverse_word_final in reverse_word:
    reverse_word1=reverse_number_final.lower()+reverse_word1
    reverse_word2=reverse_word2+reverse_number_final.lower()
if reverse_word1==reverse_word2:
    print(reverse_word, "is a palindrom word")
else:
    print(reverse_word, " Is not a palindrom number")
count_digits=785937854
digit_count=0
while count_digits>0:
    count_digits=count_digits//10
    digit_count+=1
print(digit_count)
for num in range(1,10):
    if num%3==0 and num %5==0:
        print("FID")
    elif num%3==0:
        print("re")
    elif num%5==0:
        print("ryeir")
    else:
        print("dhsjad")
cal=0
for num in range(1,11):
    p=0
    for num1 in range(1,num+1):
        if num1!=0 and num%num1==0:
            p+=1
    if p==2:
            print(num1)
            cal+=num1
print(cal)
factorial=5
factorial_iterate=1
for num in range(1, factorial+1):
    factorial_iterate*=num
print(factorial_iterate)
pattern=8
for n in range(1, pattern+1):
    for n1 in range(1, n+1):
        print("*", end="")
    print()
given_number="794327984324"
increment=0
for num in given_number:
    if int(num)>increment:
        increment=int(num)
print(increment)
word_replace=["Jan 2023", "Feb 2023", "march 2026"]
word_replace_store=[]
for word_replace1 in word_replace:
    if word_replace1.endswith("2023"):
        update_replace= word_replace1.replace("2023", "2024")
        word_replace_store.append(update_replace)
    else:
        word_replace_store.append(word_replace1)
    #return word_replace_store
print(word_replace_store)
word_replace1=["Jan 2023", "Feb 2023", "march 2026"]
word_replace_store1=[wrd.replace("2023","2024") if wrd.endswith("2023") else wrd for wrd in word_replace1]
print(word_replace_store1)
count_letter="5435435435"
count_letter_dictionary={}
for count in count_letter:
    if count not in count_letter_dictionary:
        count_letter_dictionary[count]=0
    count_letter_dictionary[count]+=1
print(count_letter_dictionary)
def shop(shop1):
    time=0.0
    for user,user1 in shop1.items():
            time+=shop1[user]
    return round(time,2)
print(shop({"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}))
def list_full_names(name_list):
    final_name_list=[]
    for first, last in name_list.items():
        for lasts in last:
            updates_name=first+" "+lasts
            final_name_list.append(updates_name)
    return final_name_list
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
def invert_resource_dict(lists):
    swap={}
    for ship, items in lists.items():
        for item in items:
            if item in swap:
                swap[item].append(ship)
            else:
                swap[item]=[ship]
    return swap
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
def word_place(word_blah):
    alpha=""
    nmeric=""
    word_blah1=word_blah.split()
    for words in word_blah1:
        if words.isalpha():
            alpha+=words+" "
        else:
            numeric=words
    alpha=alpha.strip()
    return "{} in the mid of {}".format(alpha,numeric)
print(word_place("Jacki sherrif was a great 1989"))
def network(non):
    sir=""
    for a,b in non.items():
        sir+="{} is the name and the server id is {}".format(a,b) + "\n"
    return sir
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))
def years(year_90, year_20):
    year_20.sort()
    #year_90.extend(year_20)
    year_90.append(year_20)
    return year_90
year_90=[1996,1997,1998,1999]
year_20=[2003,2004,2005,2001]
print(years(year_90,year_20))
squre=[n for n in range(1,11) if n%2==0]
print(squre)
for n in range(1,11):
    if n%2==0:
        print(n)
even=[n*n for n in range(1,11)]
print(even)
for n in range(1,11):
    res=n*n
    print(res)
condiiton=[f"{num} even" if num%2==0 else f"{num} odd" for num in range(1,11)]
print(condiiton)
flatten=[[1, 2], [3, 4], [5, 6]]
fit=[reslt for res in flatten for reslt in res]
#print(fit)
ni=[]
for n in flatten:
    for nii in n:
        ni.append(nii)
print(ni)
list_a=[1, 2, 3, 4] 
list_b=[3, 4, 5, 6]
list_c=[]
for list in list_a:
    if list in list_b:
        list_c.append(list)
print(list_c)
list_d=[listing for listing in list_a if listing in list_b]
print(list_d)
re=["hello", "world", "python"]
rim=[kin[::-1] for kin in re]
print(rim)
kia=[5, 15, 25, 35, 45]
kii=[kian+10 for kian in kia if kian%5==0]
print(kii)
for kian in kia:
    if kian%5==0:
        kkk=kian+10
        print(kkk)
dictionary_task="apple banana apple orange banana apple"
dictionary_1={}
dictionary_task1=dictionary_task.split()
for dic in dictionary_task1:
    if dic in dictionary_1:
        dictionary_1[dic]+=1
    else:    
        dictionary_1[dic]=1
#return dictionary_1
print(dictionary_1)
dic_sq={}
for n in range(1,11):
    qu=n*n
    dic_sq[n]=qu
print(dic_sq)
input= {"a": 1, "b": 2, "c": 3}
dic_inv={}
for keyy, valuee in input.items():
    dic_inv[valuee]=keyy
print(dic_inv)
fil= {"a": 5, "b": 15, "c": 8, "d": 20}
dic_fil={}
for kay, velue in fil.items():
    if velue>10:
        dic_fil[kay]=velue
print(dic_fil)
input= ["apple", "banana", "apricot", "blueberry", "cherry"]
input_dic={}
for qaz in input:
    input_first=input[0]
    if qaz in input_dic:
        input_dic[input_first].append(qaz)
    else:
        input_dic[input_first]=[]    
print(input_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY", "State": "TN"}, {"age": 30, "city": "LA"}]
fina= {name:detail for name,detail in zip(names,details)}
print(fina)
input11="hello world"
inpu_dic={}
for n in input11:
    inpu_dic[n]+=1
print(inpu_dic)
