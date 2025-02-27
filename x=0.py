x=4
while x<5:
    print("Not there "+str(x))
    x=x+1
print("x=" + str(x))

'''
def fn(x):
    n=-9
    while n <= x:
        print("Attempt " + str(n))
        n += 1
    print("Done")
fn(5)


variab=6
while variab<=10:
    print("I am genius")
    variab+=1
print("Done")

x=1
sum=0
while x<10:
    sum=sum+x
    x=x+1
#print(sum)
product = 1
while x < 10:
    product = product * x
    x = x + 1
print(product, sum)

multi=1
result=multi*5
while result<=50:
    print(result)
    multi+=1
    result=multi*5
print("Done")

prime=2
while prime<10:
    if prime / prime==1 and prime % 2 != 0 or prime ==2:
        print(prime)
    prime+=1
    
prime = 2  # Initialize prime to 2
while prime < 10:
    if prime == 2 or (prime % 2 != 0 and all(prime % i != 0 for i in range(2, int(prime ** 0.5) + 1))):
        print(prime)
    prime += 1
    
vari=6
while vari<10:
    print("Less than 10")
    vari+=1
print("Value of vari is " + str(vari))
'''
def count_number(numerical):
    fact=1
    count=0
    if numerical==0:
        return 0
    while fact<numerical:
        if numerical%fact==0:
            count+=1
        fact+=1
    return count
print(count_number(0))
print(count_number(3))
print(count_number(15))
print(count_number(20))
'''
def count_number(given_number):
    factor=1
    count=1
    if given_number==0:
        return 0
    while factor< given_number:
        if given_number%factor==0:
            count+=1
        factor+=1
    return count
print(count_number(3))
print(count_number(10))
'''

def assign_number(to_Add):
    counting=3
    starting=1
    while counting<=5:
        my_num=to_Add+counting
        if my_num>20:
            break
        print(str(counting) ,"+", str(to_Add), "=" ,str(my_num))
        counting+=1
assign_number(17)
#sum of even numbers
sum=0
for x in range(1,11):
    if x%2==0:
        print(x,"Even number")
        sum+=x
print(sum)


    
    