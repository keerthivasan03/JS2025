multiplier=5
for x in range(1,11):
    five_tabels=multiplier*x
    print(multiplier, "X", x, "=",  five_tabels)

sum_of_even_numbers=0
for x in range(1,11):
    if x%2==0:
        print(x, "is the even number")
        sum_of_even_numbers+=x
print(sum_of_even_numbers)

number_reverse="898798791"
storage=""
for x in number_reverse:
    storage=x+storage
print(storage)

count_digit=5489658435
digit_count=0
while count_digit==0:
    digit_count=1
while count_digit>0:
    count_digit=count_digit//10
    digit_count+=1
print(digit_count)

for x in range(1,101):
    if (x%3==0 and x%5==0):
        print(x, "FizzBizz")
    elif(x%3==0):
        print(x, "Fizz")
    elif(x%5==0):
        print(x, "Bizz")
    else:
        print(x, "No FizzBizz")


prime_number_count=0
for x in range(1,11):
    prime_number=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            prime_number+=1
    if prime_number==2:
            print(y, "is the prime number")
            prime_number_count+=y
print(prime_number_count)

factorial=5
factorial_result=1
for x in range(1, factorial+1):
    factorial_result*=x
print(factorial_result)

pattern=3
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("8", end="")
    print()

palindrome_number="324324"
palindrome_storage=""
for x in palindrome_number:
    palindrome_storage=x+palindrome_storage
print(palindrome_storage)
if(palindrome_storage==palindrome_number):
    print("Is a Palindrome number")
else:
    print("It is not a palindrome number")

word_palindrome="Never odd Or Even"
word_palindrome_storage1=""
word_palindrome_storage2=""
for word_palindrome_output in word_palindrome:
    if word_palindrome_output!=" ":
        word_palindrome_storage1=word_palindrome_output.upper()+word_palindrome_storage1
        word_palindrome_storage2=word_palindrome_storage2+word_palindrome_output.upper()
print(word_palindrome_storage1)
print(word_palindrome_storage2)
if(word_palindrome_storage2==word_palindrome_storage1):
    print("It is a palindorme reverse")
else:
    print("It is not a palindrome word")

digit="543543581"
largest_digit=0
for input in digit:
    if int(input)>largest_digit:
        largest_digit=int(input)
print(largest_digit)

"""years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]

for year in years:
    if year.endswith("2023"):
        new_year=year.replace("2023","2025")
        updated_years.append(new_year)
    else:
        updated_years.append(year)
print(updated_years)
"""
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[ year.replace("2024","2023") if year.endswith("2024") else year for year in years]
print(updated_years)

count_letter="5435435435"
print(len(count_letter))
count_each_time={}
for x in count_letter:
    if x not in count_each_time:
        count_each_time[x]=0
    count_each_time[x]+=1
print(count_each_time)

def add_values(values):
    time=0
    for user,value in values.items():
        time+=FileServer[user]
    return round(time, 2)

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(add_values(FileServer))

def list_full_names(name):
    name_storage={}
    for first, last in name.items():
        full_name=[]
        for lasts in last:
            output=first+" "+lasts
            full_name.append(output)
            name_storage[first] =full_name
    return name_storage
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

def invert_resource_dict(shop):
    swapping={}
    for device,types in shop.items():
        for type in types:
            if type in swapping:
                swapping[type].append(device)
            else:
                swapping[type]=[device]  
    return swapping

print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))

def word_place(text):
    input2=""
    input3=""
    input1=text.split()
    for x in input1:
        if x.isalpha():
            input2+=x+" "
        else:
            input3=x
        input3= input3.strip()
    input2=input2.strip()    
    print("{} actor at {}".format(input2,input3))
word_place("Jacki sherrif was a great 1989")

def year_add(year_90, year_20):
    year_20.sort()
    year_90.extend(year_20)
    return year_90
year_90=[1997,1998,1999]
year_20=[2000,2003,2002,2001]
print(year_add(year_90, year_20))

def year_calculate(sta, en):
    out=[year_calculate for year_calculate in range(sta, en+1)]
    print(out)
year_calculate(1977, 2002)

def square(sta_dig, end_dig):
    out1=[n*n for n in range(sta_dig, end_dig+1)]
    out2=[n*n for n in (sta_dig, end_dig)]
    print(out1)
    print(out2)
square(4,9)

def network(server):
    sepr=""
    for serv,address in server.items():
        sepr+="The server named {} have the address {}".format(serv,address) + "\n"
    return sepr
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))