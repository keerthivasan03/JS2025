multiplication=5
for n in range(1,11):
    result=n*multiplication
    print(result)

even_numbers=0
for n in range(1,11):
    if n%2==0:
        print(n, "Is the even number")
        even_numbers+=n
    else:
        print(n, "Odd number")
print(even_numbers)

resvese_number="78957984354"
reverse=""
for n in resvese_number:
    reverse=n+reverse
print(reverse)

reverse_word="Never odd or even"
store1=""
store2=""
for n in reverse_word:
    if n!=" ":
        store1=n.lower()+store1
        store2=store2+n.lower()
if store2==store1:
        print(reverse_word, "Is a palindromr word")
else:
        print(reverse_word,"Is not a palindrome word")

palindrome="121"
palindrome_check=""
for n in palindrome:
    palindrome_check=n+palindrome_check
if palindrome_check==palindrome:
     print(palindrome, "Is a Palindrome number")
else:
     print(palindrome, "Is not a palindrome numebr")

count_number=1434234
digit=0
while count_number>0:
     count_number=count_number//10
     digit+=1
print(digit)

for n in range(1,101):
    if (n%3==0) and (n%5==0):
          print(n, "FIZZBIZZ")
    elif (n%5==0):
         print(n, "Fizz")
    elif (n%3==0):
         print(n, "bizz")
    else:
         print(n, "Not a FizzBizz")

sum=0
for n in range(1,11):
    prime_number=0
    for x in range(1, n+1):
        if x!=0 and n%x==0:
            prime_number+=1
    if prime_number==2:
            print(x)
            sum+=x
print(sum)

factorial=5
queue=1
for n in range(1, factorial+1):
    queue*=n
print(queue)
    
pattern=5
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("*", end="")
    print()

largest_number="65749858645"
compare=0
for q in largest_number:
    if int(q)>compare:
        compare=int(q)
print(compare)

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
        new=year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)  

years1 = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years1=[year1.replace("2023", "2024") if year1.endswith("2023") else year1 for year1 in years1 ]
print(updated_years1)

count_letter="keert hi vasana"
letter_save={}
for n in count_letter:
    if n!=" ":
        if n not in letter_save:    
            letter_save[n]=0
        letter_save[n]+=1
print(letter_save) 

def increment(numericals):
    time=0
    for user,value in numericals.items():
       time+=FileServer[user]
    return round(time, 2)      
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(increment(FileServer))

def list_full_names(name_list):
    full=[]
    for first, lasts in name_list.items():
        for last in lasts:
            news=first+" "+last
            full.append(news)
    return full
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

def invert_resource_dict(shop):
    fin={} 
    for main, type in shop.items():
        for types in type:
            if types in fin:
                fin[types].append(main)
            else:
                fin[types]= [main]
    return fin
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))

def word_place(nun):
    input1=""
    input2=""
    nun1=nun.split()
    for n in nun1:
        if n.isalpha():
            input1+=n+" "
        else:
            input2=n
    return "{} id s fds {}".format(input1,input2)
print(word_place("Jacki sherrif was a great 1989"))

def network(dube):
    nnn=""
    for server,number in dube.items():
        nnn+="Name is{} with id {}".format(server,number) + "\n"
    return nnn

print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

def year_add(year_90, year_20):
    year_20.sort()
    year_90.extend(year_20)
    return year_90
year_90=[1997,1998,1999]
year_20=[2000,2003,2002,2001]
print(year_add(year_90, year_20))

def squre(start, end):
    res1=[n*n for n in range(start, end+1)]
    print(res1)
squre(1,10)
even_numbers=[n%2==0 for n in range(1,20)]
even_numbers1=[n for n in range(1,20) if n%2==0]
print(even_numbers)
print(even_numbers1)
condition=["even" if num%2==0 else "odd" for num in range(1,11) ]
print(condition)
Flatten=[[1, 2], [3, 4], [5, 6]] 
return_list=[final for sub_list in Flatten for final in sub_list]
print(return_list)
latten=[[1, 2], [3, 4], [5, 6]]
fine=[]
for lose in latten:
    for finse in lose:
        fine.append(finse)
print(fine)

in1=[1, 2, 3, 4] 
in2=[3, 4, 5, 6]
inout=[oo for oo in in1 if oo in in2]
print(inout)

in3=[1, 2, 3, 4] 
in4=[3, 4, 5, 6]
inn=[]
for kiss in in4:
    if kiss in in3:
        inn.append(kiss)
print(inn)

inn=["hello", "world", "python"]
retur=[kin[::-1]for kin in inn]
print(retur)

pin=[5, 15, 25, 35, 45,54]
addd=[add+10 for add in pin if add%5==0]
print(addd)

pin1=[5, 15, 25, 35, 45,54]
for x in pin1:
    if x%5==0:
        add=x+10
        print(add)

def Input(Input1):
    output={}
    inputt=Input1.split()
    for ink in inputt:
        if ink not in output:
            output[ink]=0
        output[ink]+=1
    return output
print(Input("apple banana apple orange banana apple"))

def input(squ):
    outs={}
    for x in range(1,squ+1):
        fii=x*x
        outs[x]=fii
    return outs
print(input(5))
    
def input(invert):
    sw={}
    for a,b in invert.items():
        sw[b]=a
    return sw
print(input({"a": 1, "b": 2, "c": 3}))

def input(greater_10):
    change={}
    for x,y in greater_10.items():
        if y>10:
            change[x]=y
    return change
print(input({"a": 5, "b": 15, "c": 8, "d": 20}))

def inputk(first_letter):
    first={}
    for first_letters in first_letter:
        group=first_letters[0]
        if group not in first:
            first[group]=[]
        first[group].append(first_letters)
    return first

print(inputk(["apple", "banana", "apricot", "blueberry", "cherry"]))

names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]

finn={name: detail for name, detail in zip(names,details)}
print(finn)

def charac(fre):
    storage={}
    for kia in fre:
        if kia!=" ":
            if kia in storage:
                storage[kia]+=1
            else:
                storage[kia]=1
    return storage
print(charac("hello world"))