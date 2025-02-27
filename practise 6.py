for x in range(1,16):
    if x%3==0 and x%5==0:
        print(x, "fixxbizz")
    elif x%3==0 :
        print(x, "bizz")
    elif x%5==0:
        print(x, "fixx")
    else:
        print(x, "Is not divisible by both 3 & 5")

n=10
sum=0
for x in range(1,n+1):
    prime=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            prime+=1
    if prime==2:
        print(y, "Is the prime number")
        sum+=y
print(sum," is the sum of all prime number")

factorial=5
multi=1
for x in range(1, factorial+1):
    multi*=x
print(multi, "Is the factorial of 5")

pattern=5
for a in range(1, pattern+1):
    for b in range(1,a+1):
        print("&", end="")
    print()

palindrome="125"
store=""
for x in palindrome:
    store=x+store
print(store)
if palindrome==store:
    print(palindrome, " Is a palindrome number")
else:
    print(palindrome, " is not a palindrome number")

word_palindrome="Never odd or even"
remove1=""
remove2=""
for letter in word_palindrome:
    if letter!=" ":
        remove1=remove1 + letter.lower()
        remove2=letter.lower() + remove2
if remove2==remove1:
        print(word_palindrome, "is the palindrome")
else:
        print(word_palindrome, " is not a palindrome")
print(word_palindrome.lower())

largest_digit=768943
save=0
if largest_digit==0:
    save=1
while largest_digit>0:
    largest_digit=largest_digit//10
    save+=1
print(save)

multiply= 5
for x in range(1,11):
    tabels=multiply*x
    print(multiply, "X", x, "=" , tabels)

sum=0
for x in range(1,11):
    
    if x%2==0:
        print(x, " is the even number")
        sum+=x
print(sum)

reverse_number="432431"
reversing=""
for x in reverse_number:
    reversing=x+reversing
print(reversing)

y="3219"
final=0
for q in y:
    if int(q)>final:
        final=int(q)
print(final)

def get_sentence(sentence, n):
    if n>0:
        words=sentence.split()
        if n<=len(words):
            return words[n-1]
    return ""
print(get_sentence("I am the hero of my story", 4))

Fruits=[1,2,3,4,5,"list"]
Fruits.append(6)
Fruits.insert(55,99)
Fruits.remove("list")
Fruits.pop(1)
Fruits[2]="123"
print(Fruits.reverse())

print (Fruits)

multiple=[]
for x in range(1,11):
    multiple.append(x*7)
print(multiple)

multiples=[x*7 for x in range(1,11)]
print(multiples)

out=[x for x in range(1,100) if x%3==0]
print(out)

def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8


        
