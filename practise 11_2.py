def square_of_number(number):
    square=[n*n for n in range(1, number+1)]
    print(square)
square_of_number(10)

def square_of_number1(number1):
    for n in range(1,number1+1):
        out=n*n
        print(out)
square_of_number1(10)

def even_number(number2):
    even=[n for n in range(1,number2+1) if n%2==0]
    print(even)
even_number(10)
def even_number1(number3):
    for x in range(1, number3+1):
        if x%2==0:
            print(x)
even_number(20)

def condition(number4):
    condi=[ "even" if n%2==0 else "odd" for n in range(1,number4+1)]
    print(condi)
condition(10)
def condition1(number5):
    for x in range(1,number5+1):
        if x%2==0:
            print("even")
        else:
            print("odd")
condition1(10)
flat_list=[[1, 2], [3, 4], [5, 6]] 
flat=[item for sub_item in flat_list for item in sub_item]
print(flat)
flat_list1=[[1, 2], [3, 4], [5, 6]] 
flat12=[]
for falt1 in flat_list1:
    for flat1 in falt1:
        flat12.append(flat1)
        print(flat1)

listu1=[1, 2, 3, 4] 
listuu1= [3, 4, 5, 6]
comm=[lis for lis in listu1 if lis in listuu1]
print(comm)

listu=[1, 2, 3, 4] 
listuu= [3, 4, 5, 6]
common=[]
for lis in listu:
    if lis in listuu:
        common.append(lis)
print(common) 

mul_5=[5, 15, 25, 35, 45]
nu=[n+10 for n in mul_5 if n%5==0 ]
print(nu)
Add_10=[5, 15, 25, 35, 45,51]
for x in Add_10:
    if x%5==0:
        res=x+10
        print(res)

ven=["hello", "world", "python"]
st=[]
for x in ven:
    st=(x[::-1])
    print(st)
venna=["hello", "world", "python"]
fin=[via[::-1] for via in venna]
print(fin)

def word_frequency_counter(counter):
    count={}
    spoil=counter.split()
    for x in spoil:
        if x not in count:
            count[x]=0
        count[x]+=1
    return count
print(word_frequency_counter("apple banana apple orange banana apple"))

def squares(end):
    dic={}
    for x in range(1,end+1):
        double=x*x
        dic[x]=double
    return dic
print(squares(5))

def invert(kv):
    invert_storage={}
    for key,value in kv.items():
        invert_storage[value]=key
    return invert_storage
print(invert({"a": 1, "b": 2, "c": 3}))

def greater(than_10):
    final_value={}
    for alpha, numeric in than_10.items():
        if numeric>10:
            final_value[alpha]=numeric
    return final_value
print(greater({"a": 5, "b": 15, "c": 8, "d": 20}))

def group(first):
    final_letter={}
    for word in first:
        single=word[0]
        if single not in final_letter:
            final_letter[single]=[]
        final_letter[single].append(word)
    return final_letter
print(group(["apple", "banana", "apricot", "blueberry", "cherry"]))

names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY"}, {"age": 30, "city": "LA"}]

nested_dic={name: detail for name, detail in zip(names, details)}
print("\n")
print(nested_dic)

def character_freq(charcater):
    freq={}
    for char in charcater:
        if char!=" ":
            if char in freq:    
                freq[char]+=1
            else:
                freq[char]=1
    return freq
print(character_freq("Hello world"))


dict1 = {"a": 10, "b": 20}
dict2 = {"b": 5, "c": 15}

common_word = dict1.copy()  # Copy dict1
print("Before updating:", common_word)

for key, value in dict2.items():
    if key in common_word:
        common_word[key] += value  # Add values for common keys
    else:
        common_word[key] = value  # Add new key-value pairs

print("After updating:", common_word)

# Create a dictionary where keys are numbers from 1 to 10 and values are "Even" or "Odd"
even_odd_dict = {num: "Even" if num % 2 == 0 else "Odd" for num in range(1, 11)}
print(even_odd_dict)
# Output: {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', ..., 10: 'Even'}

"""def condition(number4):
    condi=[ "even" if n%2==0 else "odd" for n in range(1,number4+1)]
    print(condi)
condition(10)
def condition1(number5):
    for x in range(1,number5+1):
        if x%2==0:
            print("even")
        else:
            print("odd")
condition1(10)
"""
# Write a dictionary comprehension to map words to their lengths
words = ["python", "java", "c++"]
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)
# Output: {'python': 6, 'java': 4, 'c++': 3}

# Flatten a dictionary where values are lists into a single list
input_dict = {"a": [1, 2], "b": [3, 4], "c": [5]}
flattened_list = [value for values in input_dict.values() for value in values]
print(flattened_list)
# Output: [1, 2, 3, 4, 5]

"""flat_list=[[1, 2], [3, 4], [5, 6]] 
flat=[item for sub_item in flat_list for item in sub_item]
print(flat)
flat_list1=[[1, 2], [3, 4], [5, 6]] 
flat12=[]
for falt1 in flat_list1:
    for flat1 in falt1:
        flat12.append(flat1)
        print(flat1)
        
listu1=[1, 2, 3, 4] 
listuu1= [3, 4, 5, 6]
comm=[lis for lis in listu1 if lis in listuu1]
print(comm)

listu=[1, 2, 3, 4] 
listuu= [3, 4, 5, 6]
common=[]
for lis in listu:
    if lis in listuu:
        common.append(lis)
print(common) 
"""






