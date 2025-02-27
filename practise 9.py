input="4324923"
output=0
if input==0:
    output=0
for inputs in input:
    if  int(inputs)>output:
        output=int(inputs)
print(output, " is the largest digit in the given sequence")

palindrome_number="121"
palindrome_final=""
for x in palindrome_number:
    palindrome_final=x+palindrome_final
print(palindrome_final)
if (palindrome_final==palindrome_number):
    print(palindrome_number, " Is a a palindrome number")
else:
    print(palindrome_number, "Is not a Palindrom number")

word_palindrome="Never Odd or even"
original_lower=""
reverse_lower=""
for x in word_palindrome:
    if x!=" ":
        reverse_lower=x+reverse_lower
        original_lower=original_lower+x
print(reverse_lower)
if (reverse_lower==original_lower):
        print("Palindrome")
else:
        ("Not a Palindrome")

Pattern=5
for x in range(1,Pattern+1):
    for y in range(1, x+1):
        print("o", end="")
    print()

factorial=5
out=1
for x in range(1,factorial+1):
     out*=x
print(out)

prime_number=10
sums=0
for q in range(1,prime_number+1):
    incre=0
    
    for w in range(1,q+1):
        if w!=0 and q%w==0:
            incre+=1
    if incre==2:
            print(w)
            sums+=w
print(sums)

for x in range(1,101):
    if (x%3==0 and x%5==0):
        print(x, "FizzBizz")
    elif (x%3==0 ):
          print(x, "Fizz")
    elif (x%5==0):
          print(x, "Bizz")
    else:
         print(x," Not FizzBizz")

count_digit=524324324
count=0
while count_digit:
        count_digit=count_digit//10
        count+=1
print(count)

summ=0
for x in range(1,11):
    if(x%2==0):
        print(x)
        summ+=x
print(summ)

multiplier=5
for x in range(1,11):
     res=multiplier*x
     print("{} X {} = {}".format(multiplier,x,res))

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for year in years:
     if year!=" ":
        new=year.replace("2023","2024")
        updated_years.append(new)
     else:
          updated_years.append(year)
print(updated_years)

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years= [year.replace("2023","2024") if year.endswith("2023") else year for year in years]
print(updated_years)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
"jpg" in file_counts
"html" in file_counts

file_count = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_count.items():
  print("There are {} files with the .{} extension".format(amount, ext))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys()
file_counts.values()

def count_letters(txt):
 ress={}
 for letter in txt:
    if letter not in ress:
         ress[letter]=0
    ress[letter]+=1
 return ress
print(count_letters("aaaa"))
print(count_letters("keerthivsn"))    

def sum_server_use_time(Server):
    tota_time=0.0
    for key,value in Server.items():
         tota_time+=Server[key]
    return round(tota_time, 2)
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer))

def list_full_names(boss):
    storage=[]
    for first, lasts in boss.items():
        for last in lasts:
               full_name= (first+" " +last)
               storage.append(full_name)
    return  storage   
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))


def invert_resource_dict(res):
    sav={}
    for resource_group, resource in res.items():
        for resources in resource:
            if resources in sav:
                  sav[resources].append(resource_group)
            else:
                 sav[resources]=[resource_group]
    return sav
             
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


     
        

