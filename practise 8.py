multiply=5
for x in range(1,11):
    multiply_Result= multiply*x
    print(multiply, "X", x ,"=" , multiply_Result)


for x in range(1,11):
    sum=0
    if x%2==0:
        print(x, "is the even number")
        sum+=x
print(sum)

reverse_number="121"
reverse=""
for x in reverse_number:
    reverse=x+reverse
print(reverse)
if (reverse==reverse_number):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")

word_palindrome="Never odd or evens"
rev1=""
rev2=""
for x in word_palindrome:
    if x!=" ":
        rev1=x.lower()+rev1
        rev2=rev2+x.lower()
if rev1==rev2:
        print("It is a palindrome")
else:
        print("It is not a palindrome")

count_digit=45332
count=0
if count_digit==0:
     count=1
while count_digit>0:
     count_digit=count_digit//10
     count+=1
print(count)

end=100
for x in range(1,end+1):
    if x%3==0 and x%5==0:
          print(x, "fizzbizz")
    elif x%3==0:
         print(x, "fizz")
    elif x%5==0:
         print(x, "Bizz")
    else:
         print(x, "Not a fizzbizz")

sum1=0
for x in range(1,11):
    prime=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            prime+=1
            #sum+=y
    if prime==2:
        print(y, "Is the prime number")
        sum1+=y
print(sum1)

factorial=5
factorial_output=1
for x in range(1, factorial+1):
     factorial_output*=x
print(factorial_output)

pattern=5
for x in range(1, pattern+1):
     for y in range(1, x+1):
        print("F", end="")
     print()

largest_digit="8765432190"
largest_digit_output=0
if largest_digit==0:
    largest_digit_output=0
for x in largest_digit:
     if int(x)>largest_digit_output:
        largest_digit_output=int(x)
print(largest_digit_output)

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years=[]
for year in years:
    if year.endswith("2023"):
         new=year.replace("2023","2024")
         updated_years.append(new)
    else:
         updated_years.append(year)
print(updated_years) 

yearings = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_yearing=[yearing.replace("2023", "2024") if yearing.endswith("2023") else yearing for yearing in yearings]
print(updated_years)

     



    
           
