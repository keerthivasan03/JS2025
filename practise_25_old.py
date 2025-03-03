#multiplicatin
to_be_mulitplied=5
for x in range(1,11):
    multiply_result=x* to_be_mulitplied
    print(x,"*", to_be_mulitplied,"=",multiply_result)
#sum of even nmber
sum_of_even=0
for x in range(1,11):
    if x%2==0:
        print(x, "evennumbr")
        sum_of_even+=x
print(sum_of_even)
#reverse_number
reverse_number="1234"
reversed_number=""
for x in reverse_number:
    reversed_number=x+reversed_number
print(reversed_number)
#count digits
count_digit=4324243
counted_digit=0
while count_digit>0:
    count_digit=count_digit//10
    counted_digit+=1
print(counted_digit)
#FizzBizz
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x,"FizzBizz")
    elif x%3==0:
        print(x,"Bizz")
    elif x%5==0:
        print(x, "Fizz")
    else:
        print(x, "No FizzBizz")
sum_prime=0
for x in range(1,11):
    count_prime=0
    for y in range(1,x+1):
        if x%y==0 and y!=0:
            count_prime+=1
    if count_prime==2:
            print(y, "prime number")
            sum_prime+=y
print(sum_prime)
#factorial
factorial=5
fact_mul=1
for x in range(1,factorial+1):
    fact_mul*=x
print(fact_mul)
#pattern
for x in range(1,9):
    for y in range(1,x+1):
        print("X", end="")
    print()
#palindrome_check
palidrome_number="121"
palindrome_save=""
for x in palidrome_number:
    palindrome_save=x+palindrome_save
print(palindrome_save)
if palindrome_save==palidrome_number:
    print(palidrome_number,"is a palindrome number")
else:
    print(palidrome_number,"Not a palindrome number")
#largest number
largest="43234324080932"
digit=0
for x in largest:
    if int(x)>digit:
        digit=int(x)
print(digit)
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for x in years:
    if x.endswith("2025"):
        new_year=x.replace("2025","2024")
        updated_years.append(new_year)
    else:
        updated_years.append(x)
print(updated_years)
names=["Keerthi vasan", "Keerthi hasah","waste"]
updated_names=[]
for x in names:
    if x.startswith("Keerthi"):
        new_name=x.replace("Keerthi", "Waste")
        updated_names.append(new_name)
    else:
        updated_names.append(x)
print(updated_names)
count_letter="5435435435"
count_dic={}
for x in count_letter:
    if x in count_dic:
        count_dic[x]+=1
    else:
        count_dic[x]=1
print(count_dic)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0
for enduser,times in FileServer.items():
    time+=times
print(round(time,2))
list_full_names={"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}
new_one=[]
for first,last in list_full_names.items():
    for lasst in last:
        new_updated=first + " "+ lasst
        new_one.append(new_updated)
print(new_one)
invert_resource_dict={"Hard Drives": ["IDE HDDs", "SCSI HDDs","poda venna"],"PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}
invert_dic={}
for device, ec in invert_resource_dict.items():
    for ecs in ec:
        if ecs in invert_dic:
            invert_dic[ecs]+=[device]
        else:
            invert_dic[ecs]=[device]
print(invert_dic)
word_place="Jacki sherrif was a great 1989"
alpha=""
numeric=""
word_place_split=word_place.split()
for x in word_place_split:
    if x.isalpha():
        alpha+=x+" "
    else:
        numeric+=x
alpha=alpha.strip()
print("{} at {}".format(alpha,numeric))
network={"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}
network_list=""
for domain,id in network.items():
    network_list+="{} is the id for {}".format(domain,id)+"\n"
print(network_list)
#square_number:
square=[x*x for x in range(1,11)]
print(square)
#Even_number:
even=[x for x in range(1,11) if x%2==0]
print(even)
#conditional
conditional=[{x: "even"} if x%2==0 else {x: "odd"} for x in range(1,11)]
print(conditional)
#flatten
flat_list=[[1, 2], [3, 4], [5, 6]]
flat_append=[]
for flat in flat_list:
    for flas in flat:
        flat_append.append(flas)
print(flat_append)
comm1=[1, 2, 3, 4] 
comm2=[3, 4, 5, 6]
comm3=[]
for comm in comm2:
    if comm in comm1:
        comm3.append(comm)
print(comm3)
reverse_word=["hello", "world", "python"]
updated_reverse=[nnn[::-1] for nnn in reverse_word] 
print(updated_reverse)
filter_transform=[5, 15, 25, 35, 45,32]
for x in filter_transform:
    if x%5==0:
        x+=10
        print(x)
word_dic="apple banana apple orange banana apple"
word_dic_save={}
word_dic_split=word_dic.split()
for x in word_dic_split:
    if x in word_dic_save:
        word_dic_save[x]+=1
    else:
        word_dic_save[x]=1
print(word_dic_save)
#squre
sq_dic={}
for x in range(1,101):
    sq_res=x*x
    sq_dic[x]=sq_res
print(sq_dic)
Innput= {"a": 1, "b": 2, "c": 3}
Innput_dic={}
for a,b in Innput.items():
    Innput_dic[b]=[a]
print(Innput_dic)
fiter={"a": 5, "b": 15, "c": 8, "d": 20}
fiter_dic={}
for a,b in fiter.items():
    if b>5:
        fiter_dic[a]=b
print(fiter_dic)
groups=["apple", "banana", "apricot", "blueberry", "cherry"]
groups_dic={}
for x in groups:
    groups_first=x[0]
    if groups_first in groups_dic:
        groups_dic[groups_first]+= [x]
    else:
        groups_dic[groups_first]=[x]
print(groups_dic)
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]
updated_list={name:detail for name, detail in zip(names,details)}
print(updated_list)
charater_freq="hello world"
charater_dic={}
for x in charater_freq:
        if x!=" ":
            if x in charater_dic:     
                charater_dic[x]+=1
            else:
                charater_dic[x]=1
print(charater_dic)
in1= {"a": 10, "b": 20}
in2= {"b": 5, "c": 15}
update_in=in1.copy()
for a,b in in2.items():
    if a in update_in:
        update_in[a]+=b
    else:
        update_in[a]=b
print(update_in)
dic_len=["python", "java", "c++"]
len_dic={}
for x in dic_len:
    word_len=len(x)
    len_dic[x]=word_len
print(len_dic)
join= {"a": [1, 2], "b": [3, 4], "c": [5]}
updated_join=[]
for a,b in join.items():
    updated_join.extend(b)
print(updated_join)
reverse_particular_word="I am learning python"
word_to_reverse=reverse_particular_word[5:13]
word_save=""
for x in word_to_reverse:
    word_save=x+word_save
reverse_update=(reverse_particular_word[:5]+word_save+reverse_particular_word[13:])
print(reverse_update)
palindrome_word="Never odd or even"
palindrome1=""
palindrome2=""
for x in palindrome_word:
    if x!=" ":
        palindrome1=x.lower()+palindrome1
        palindrome2=palindrome2+x.lower()
print(palindrome1, palindrome2)
if palindrome2==palindrome1:
    print(palindrome_word,"Is Palindrome")
else:
    print(palindrome_word,"Not palindrome")