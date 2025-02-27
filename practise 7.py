multiplier=5
multiple=[x*multiplier for x in range(1,11)]
for x in range(1,11):
    print(multiplier, "X", x, "=" , x*multiplier )

n=10
even_number=[x%2==0 for x in range(1,11)]
print(even_number)

n=10
even=[x for x in range(1,11) if x%2==0]
print(even)

sum=0
for x in range(1,11):
    if x%2==0:
        print(x)
        sum+=x    
print(sum)

reverse_numer="121"
reverse=""
for x in reverse_numer:
    reverse=x+reverse
print(reverse)
if reverse==reverse_numer:
    print("Is Palindrome")
else:
    print("Not Palindrome")

count_digit=543754
digi=0
if count_digit==0:
    digi=1
while count_digit > 1:
    count_digit=count_digit//10
    digi+=1
print(digi)

q=100
for x in range(1,q+1):
    if x%3==0 and x%5==0:
        print(x, "Fizz Bizz")
    elif x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Bizz")
    else:
        print(x, "Not divisible by 3 & 5")


ran=100
for m in range(1,ran+1):
    cout=0
    for o in range(1,m+1):
        if o!=0 and m%o==0:
            cout+=1
    if cout==2:
        print(o)

factoriql=5
fact=1
for x in range(1,factoriql+1):
    fact*=x
print(fact)

pattern=5
for x in range(1, pattern+1):
    for y in range(1,x+1):
        print("E", end="")
    print()

largest_digit="56438"
start=0
if largest_digit==0:
    start=1
for x in largest_digit:
    if int(x) > start:
        start=int(x)
print(start)

reversible_check="keerthi vasan"
check=""
check1=""
for x in reversible_check:
    if x!=" ":
        check=x.lower()+check
        check1=check1+x.lower()
print(check1, check)
