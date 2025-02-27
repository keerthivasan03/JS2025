multi=5
for x in range(1,11):
    r=multi*x
    print(multi, "X", x, "=", r)

add=0
for x in range(1,11):
    if x%2==0:
        print(x," Is the even number")
        add+=x
print(add)

reverse="42343299"
store1=""
for x in reverse:
    store1=x+store1
print(store1)
if store1==reverse:
    print("palindrome")
else:
    print("Not a palindrome")

word_reverse="Never Odd Or Even"
store2=""
store3=""
for letter in word_reverse:
    if letter!=" ":
        store2=letter.lower()+store2
        store3=store3+letter.lower()
print(store2)
print(store3)
if(store3==store2):
    print(word_reverse, "Is a palindrome")
else:
    print(word_reverse, " Is not a palindrome")

x=0
digit=0
if x==0:
        digit=1
while x>0:
        x=x//10
        digit+=1
print(digit)

for x in range(1,101):
    if(x%3==0 and x%5==0):
        print(x, " FizzBizz")
    elif( x%5==0):
        print(x, " Fizz")
    elif(x%3==0):
        print(x, " Bizz")
    else:
        print(x, " No FizzBizz")

prime=0
for x in range(1,11):
    incre=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            incre+=1
    if incre==2:
        print(y)
        prime+=y
print(prime)

factorial=5
rum=1
for x in range(1,factorial+1):
    rum*=x
print(rum)

pattern=5
for x in range(1,pattern+1):
    for y in range(1,x+1):
        print("*", end="")
    print()

largest_digit="785439434"
digit1=0
for x in largest_digit:
    while int(x)>digit1:
        digit1=int(x)
print(digit1)

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]
for year in years:
    if year.endswith("2023"):
        new_year=year.replace("2023","2024")
        updated_years.append(new_year)
    else:
        updated_years.append(year)
print(updated_years)

yeas = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_yeas=[yea.replace("2024", "2025") if yea.endswith("2024") else yea for yea in yeas]
print(updated_yeas)

def count_letter(txt):
    dic={}
    for x in txt:
        if x not in dic:
            dic[x]=0
        dic[x]+=1
    return dic
print(count_letter("Keerthivasan"))

def sum_server_use_time(values):
    time=0
    for user,time_taken in values.items():
        time+=FileServer[user]
    return round(time, 2)

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer))

def list_full_names(names):
    init=[]
    for first_name, last_name in names.items():
        for last in last_name:
            final_name=first_name+" "+last
            init.append(final_name)
    return init
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

def invert_resource_dict(shop):
    shop_save={}
    for parts, types in shop.items():
        for type in types:
            if type in shop_save:
                shop_save[type].append(parts)
            else:
                shop_save[type]=[parts]
    return shop_save

print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
 #1
def item_price(text):
    item=""
    price=""
    item_price_list=text.split()
    for x in item_price_list:
        if x.isalpha():
            item += x+" "
        else:
            price=x
    item=item.strip()
    return "{} is the price ${}".format(item,price)
print(item_price("Jaci was the 89"))
 #2            
def uneven(pop):
    i=""
    p=""
    j= pop.split()
    for x in j:
        if x.isalpha():
            i+= x+" "
        else:
            p=x
    return "{} is the price ${}".format(i,p)

print(uneven("POda dai enalu vela iruku 900"))

def count_words(new_text):
    return len(new_text.split())
print(count_words("Catalog item 3523 : Organic raw pumpkin seeds in shell"))

def record_profit(recent_first, recent_last):
    recent_first.reverse()
    recent_last.extend(recent_first)
    return recent_last
recent_first= [2022, 2018, 2011, 2006]
recent_last= [1989, 1992, 1997, 2001]
print(record_profit(recent_first, recent_last))

def year_count(start, end):
    return [year for year in range(start, end+1)]
print(year_count(1972,1975))

def odd(numerical):
    return [n for n in range(1,numerical+1) if n%2==0]
print(odd(9))

def network(servers):
    net=""
    for a,b in servers.items():
        net+="The IP address of the {} server is {}".format(a, b) + "\n"
    return net
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

