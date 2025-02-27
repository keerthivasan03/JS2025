"""
input =5
for x in range(11):
    input1= input*x
    print(input, "X", x , "= " +str(input1))

input=10
for x in range(11):
    if x%2==0:
        print(x)
        x+=1
    
def count_num(numerical):
    count=0
    if numerical==0:
        count+=1
    while numerical>0:
        numerical=numerical//10
        count+=1
    return count
print(count_num(145764654))

reverse="1290"
print(reverse[::-1])
"""
for x in range(1,101):
        if x%3==0:
            print(str(x) +" "+ "Fizz")
        if x%5==0:
            print(str(x)+ " "+"BIzz")
        if x%3==0 and x%5==0:
            print(str(x) +" "+ "FizzBizz")
        if x%3!=0 and x%5!=0:
            print(str(x) + " "+ "Not divisible by both 3 & 5")


"""
min=0
max=11
for x in range(min,max):
    count=0    
    for y in range(min,max+1):
        if y!=0 and x%y==0:
            count+=1
    if count==2:
        print(x)
"""
"""for x in range(1, 5):
    count=1
    for y in range(1,x+1):
        count *=y
    print(count)

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *=i
    print(result)

factorial(5)

def everse(strng):
    reverese_string=""
    for cha in strng:
        reverese_string= cha+ reverese_string
    return int(reverese_string)
print(everse("12376576"))

def factt(num):
    results=1
    for num in range(1, num+1):
        results *=num
    print(results)
factt(5)

def rev(rim):
    revvv=""
    for dum in rim:
        revvv=dum+revvv
    print(int(revvv))
rev("431512")

min=0
max=11
for x in range(min,max):
    count=0
    for y in range(min,max+1):
        if y!=0 and x%y==0:
            count+=1
    if count==2:
        print(x)

def pyramid(nim):
    for x in range(nim):
        for y in range(x+1):
            print("*", end=" ")
        print()
pyramid(5)
"""
def pal(ste):
    save=""
    for split in ste:
        save=split+save
    
    if save == ste:
        print(ste + " Is a palindrome number")
    else:
        print(ste + " not a prime number")
pal("129")

def input(nnn):
    no=0
    for large in str(nnn):
        if int(large) > no:
            no=int(large)
    return no          
nnn=70324
print(f"largest number in digit is  {input(nnn)}")

def largest_number(n):
    largest=0
    for large in str(n):
        if int(large) > largest:
            largest= int(large)
    return largest
print (f"largest number is {largest_number(98765467)}")