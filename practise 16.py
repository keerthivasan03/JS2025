multiplicaiton=9
for x in range(1,11):
    result=multiplicaiton*x
    print(x, "X", multiplicaiton, "=", result)
sum=0
for x in range(1,11):
    if x%2==0:
        print(x, "Even number")
        sum+=x
print(sum)
reverse_number="43243"
reverse_number_final=""
for x in reverse_number:
    reverse_number_final=x+reverse_number_final
print(reverse_number_final)
reverse_word="Never odd or even"
reverse_number_final1=""
reverse_number_final2=""
for x in reverse_word:
    if x!=" ":
        reverse_number_final1=x.lower()+reverse_number_final1
        reverse_number_final2=reverse_number_final2+x.lower()
print(reverse_number_final2)
print(reverse_number_final1)
if (reverse_number_final1)==(reverse_number_final2):
    print("Palidntome word")
else:
    print("not")
count_digit=794735
count_digit_final=0
while count_digit>0:
    count_digit=count_digit//10
    count_digit_final+=1
print(count_digit_final)
for x in range(1,11):
    if x%3==0 and x%5==0:
        print(x, "jkfs")
    elif x%3==0:
        print(x, "hgds")
    elif x%5==0:
        print(x, "hfds")
    else:
        print(x, "fdsfd")
p=0
for x in range(1,11):
    q=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            q+=1
    if q==2:
        print(y, "Prime")
        p+=y
print(p)
factorial=9
self=1
for factorial1 in range(1, factorial+1):
    self*=factorial1
print(self)
pattern=9
for x in range(1,pattern+1):
    for y in range(1, x+1):
        print("D", end="")
    print()
largest_digit="54235952435"
iteration_Start=0
for largest_digit_iteration in largest_digit:
    if int(largest_digit_iteration)>iteration_Start:
        iteration_Start=int(largest_digit_iteration)
print(iteration_Start)
list_update=["Keerthi vasan", "Harishwadha siva"]
updated_list=[]
for list_updates in list_update:
    if list_updates.endswith("siva"):
        final_update=list_updates.replace("siva", "keerthi vasan")
        updated_list.append(final_update)
    else:
        updated_list.append(list_updates)
print(updated_list)
updated_list1=[list_updates.replace("siva", "Anu") if list_updates.endswith("siva") else list_updates for list_updates in list_update]
print(updated_list1)
count_letter="54354354355"
count_letter_dic={}
for count_letter_iteration in count_letter:
    if count_letter_iteration in count_letter_dic:
        count_letter_dic[count_letter_iteration]+=1
    else:
        count_letter_dic[count_letter_iteration]=1
print(count_letter_dic)
FileServer = {"EndUser1": 2.25787, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for user, value in FileServer.items():
    time+=FileServer[user]
print(round(time,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
updated_name_list=[]
for first, last in list_full_names.items():
    for lasts in last:
        name_list=first+" "+lasts
        updated_name_list.append(name_list)
print(updated_name_list)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert_resource_dictionary={}
for device, spare in invert_resource_dict.items():
    for spares in spare:
        if spares in invert_resource_dictionary:
            invert_resource_dictionary[spares]+=[device]
        else:
            invert_resource_dictionary[spares]=[device]
print(invert_resource_dictionary)
word_replace="Jackie sherif is the great actor in 1999"
word=""
number=""
word_replace_iteration1=word_replace.split()
for word_replace_iteration in word_replace_iteration1:
    if word_replace_iteration.isalpha():
        word+=word_replace_iteration + " "
    else:
        number+=word_replace_iteration
word=word.strip() 
print("{} his period at {}".format(word,number))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
updating=""
for dom, id in network.items():
    updating+="{} is the server name with id {}".format(dom, id) +"\n"
print(updating)
word_frequency="apple banana apple orange banana apple"
word_frequency_split= word_frequency.split()
word_frequency_dic={}
for word_frequency_update in word_frequency_split:
    if word_frequency_update in word_frequency_dic:
        word_frequency_dic[word_frequency_update]+=1
    else:
        word_frequency_dic[word_frequency_update]=1
print(word_frequency_dic)
square_dic={}
for square_dic_iter in range(1,11):
    squre= square_dic_iter*square_dic_iter
    square_dic[square_dic_iter]=squre
print(square_dic)
inverted_dictionary={"a": 1, "b": 2, "c": 3}
inver={}
for value, agn in inverted_dictionary.items():
    inver[agn]=value
print(inver)
filter_dictionary={"a": 5, "b": 15, "c": 8, "d": 20}
filter_dictionary_final={}
for value, values in filter_dictionary.items():
    if values>5:
        filter_dictionary_final[value]=values
print(filter_dictionary_final)
group_by_first_letter=["apple", "banana", "apricot", "blueberry", "cherry"]
group_by_first_letter_dic={}
for group in group_by_first_letter:
    group_first=group[0]
    if group_first in group_by_first_letter_dic:
        group_by_first_letter_dic[group_first].append(group)
    else:
        group_by_first_letter_dic[group_first]=[group]
print(group_by_first_letter_dic)
nested_dic=names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
nest=[{poda: venna} for poda, venna in zip(names, details)]
print(nest)
character_frequenc="Keekrthi vasan"
character_frequency=character_frequenc.lower()
haracter_frequecny={}
for character in character_frequency:
    if character!=" ":
        if character in haracter_frequecny:
            haracter_frequecny[character]+=1
        else:
            haracter_frequecny[character]=1
print(haracter_frequecny)
merge_dic1={"a": 10, "b": 20}
merge_dic12={"b": 5, "c": 15}
merge_dic1_copy=merge_dic1.copy()
merge_dic_final={}
for ke, val in merge_dic12.items():
    if ke in merge_dic1_copy:
        merge_dic1_copy[ke]+=val
    else:
        merge_dic1_copy[ke]=val
print(merge_dic1_copy)
for x in range(1,11):
    if x%2==0:
        print(x,"Even")
    else:
        print(x, "odd")
assign_values={x: "even" if x%2==0 else "odd" for x in range(1,11) }
print(assign_values)
word_length=["python", "java", "c++"]
word_length_final={}
for words_length in word_length:
    word_length_value=len(words_length)
    word_length_final[words_length]=word_length_value
print(word_length_final)
join={"a": [1, 2], "b": [3, 4], "c": [5,5,6]}
join_dic=set()
for value, keys in join.items():
    join_dic.update(keys)
print(join_dic)
flattern=[5, 15, 25, 35, 45]
flattern_list=[ad+10 for ad in flattern if ad%5==0]
print(flattern_list)
for flatterns in flattern:
    if flatterns%5==0:
        fit=flatterns+10
        print(fit)
reverse_list=["hello", "world", "python"]
reverse_list_last=[rev[::-1] for rev in reverse_list]
print(reverse_list_last)
merge_list_a=[1, 2, 3, 4] 
merge_list_b=[3, 4, 5, 6]
merge_list_comp=[lists for  lists in merge_list_b if lists in merge_list_a]
print(merge_list_comp)
merge_list=[]
for f2 in merge_list_a:
    if f2 in merge_list_b:
        merge_list.append(f2)
print(merge_list)
list_merge= [[1, 2], [3, 4], [5, 6]] 
list_merge_list=[listing for listu in list_merge for listing in listu]
print(list_merge_list)
lu=[]
for listings in list_merge:
    for luu in listings:
        lu.append(luu)
print(lu)
conditin_list=["even" if num%2==0 else "odd" for num in range(1,11)]
print(conditin_list)
even=[num*num for num in range(1,21)]
print(even)
