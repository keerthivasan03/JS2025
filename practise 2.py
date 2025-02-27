def multiplication(limit):
    for x in range(11):
        multiplication_result= limit*x
        #print(x + "*" + limit + "=" + multiplication_result)
        print(x , "*" , limit , "=" , multiplication_result)
multiplication(5)
#correct version
sum_final=0
for x in range(1,11):
    if x%2==0:
        print("Even number:" , x)
        sum_final+=x
print(sum_final)
#wrong version
for x in range(1,11):
    sum_final1=0    
    if x%2==0:
        print("Even number:" , x)
        sum_final1+=x
print(sum_final1)

reverse_number="123456"
reversed=""
for x in reverse_number:
    reversed=x+reversed
print(reversed)

"""def count_digit(numerical_value):

    for x in count_digit:
        count=0  
        if x==0:
            count+=1
            if x//10!=0:
                count+=1
    print(count)
count_digit(132435)
"""
def counting(numeric):
    count=0
    if numeric==0:
        count+=1
    while numeric>0:
        numeric=numeric//10
        count+=1
    return(count)
print(counting(43141))

for x in range(1,101):
    if(x%3==0 and x%5==0):
        print("Fizzbizz " + str(x))
    elif(x%3==0 ):
        print("bizz " + str(x))
    elif(x%5==0):
        print("Fizz " + str(x))
    else:
        print("Buxx "+ str(x))

#def prime(numbers):
min=1
max=11
#prime_number=0
for x in range(min,max):
        prime_number=0
        for y in range(min, max+1):
            if (y!=0 and x%y==0):
                prime_number+=1
        if prime_number==2:
            print("Prime number: " + str(x))

"""def factorial(m, multiplication):
    multi=0
    for x in range(m, multiplication):
        multi=1
        for y in range(m, multiplication+1):
            multi*=y
    print(multi)
factorial(1,6)
"""
def factorial1(n):
    mu=1
    for x in range(1, n+1):
        mu*=x
    print(mu)
factorial1(5)

def pyramid(n):
    for x in range(n):
        for y in range(x+1):
            print("X", end=" ")
        print()
pyramid(4)

def palindrome(pali):
    rev=""
    for x in pali:
        rev=x+rev
        #return rev
    print(rev)
    if rev==pali:
            print("Given number is palindrome" )
    else:
            print("not a palindrome")
    print(pali)
palindrome("191")

def largest_digit(find):
    large=0
    for x in find:
        if large<int(x):
            large=int(x)
        #return large
    print(large)
largest_digit("2781839")







