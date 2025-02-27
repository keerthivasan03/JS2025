multiplication_number=5
for x in range(1,11):
    five_tables=multiplication_number*x
    print(multiplication_number,  "* ", x , "= " +str(five_tables) )

sum=0
for y in range(1,11):
    if y%2==0:
        print(y, "Is the even number")
        sum+=y
print(sum)

reverse_number="1234"
reverse=""
for x in reverse_number:
    reverse=x+reverse
print(reverse)

count_digits=0
count=0
if count_digits==0:
    count=1
while count_digits>0:
        count_digits=count_digits//10
        count+=1
print(count)

for q in range(1,16):
     if (q%3==0) and (q%5==0):
          print(q, " FizzBizz")
     elif (q%3==0):
          print(q, " Fizz")
     elif (q%5==0):
          print(q, " Bizz")
     else:
        print(q, "Not divisible by both 5 & 3")

n=10
for a in range(1,n+1):
     prime=0
     for s in range(1,a+1):
        if s!=0 and a%s==0:
            prime+=1
     if prime==2:
             print(s, "Is the Prime number")

factorial=5
final=1
for x in range(1,factorial+1):
     final*=x
print(final)

pattern=5
for d in range(1, pattern+1):
     for f in range(1,d+1):
          print("^", end="")
     print()

palidrome="121"
palindrome_output=""
for x in palidrome:
    palindrome_output=x+palindrome_output
print(palindrome_output)
if palindrome_output==palidrome:
     print(palidrome, "is a palindrome number")
else:
     print(palidrome, "is not a palindrome number")

largest_digit="2379"
largest_output=0
for g in largest_digit:
    if int(g)>largest_output:
        largest_output=int(g)
print(largest_output)



               



