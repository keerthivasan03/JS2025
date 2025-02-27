multiplication=8
for x in range(1,6):
    multiplication_result=multiplication* x
    print(multiplication_result)
crime_number_add=0
for x in range(1,11):
    crime_number=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            crime_number+=1
    if crime_number==2:
        print(y, "is the prime number")
        crime_number_add+=y
print(crime_number_add)
reverse_number="32432432"
reverese_number_store=""
for x in reverse_number:
    reverese_number_store=x+reverese_number_store
print(reverese_number_store)
reverse_word="Never odd or even"
reverse_word_store1=""
reverese_word_store2=""
for x in reverse_word:
    if x!=" ":
        reverse_word_store1=x.lower()+reverse_word_store1
        reverese_word_store2=reverese_word_store2+x.lower()
print(reverese_word_store2)
print(reverse_word_store1)
if (reverse_word_store1==reverese_word_store2):
    print(reverse_word, "True")
else:
    print(reverse_word, "false")
reverse_single_word="keerthivasan"
reverse_single_word_1=""
for x in reverse_single_word:
    reverse_single_word_1=x+reverse_single_word_1
print(reverse_single_word_1)
if reverse_single_word_1==reverse_single_word:
    print("True")
else:
    print("false")
count_digits=5435435
count_digits_result=0
while count_digits>0:
    count_digits=count_digits//10
    count_digits_result+=1
print(count_digits_result)
#fizzbizz program
for x in range(1,11):
    if x%3==0 and x%5==0:
        print(x, "FizzBIzz")
    elif x%3==0:
        print(x, "Fizz")
    elif x%5==0:
        print(x, "Bizz")
    else:
        print(x, "no fizzbizz")
#sumof even
sum_even=0
for x in range(1,11):
    if x%2==0:
        print(x, "is even nujmber")
        sum_even+=x
print(sum_even)
#factorial
factorial=5
factorial_result=1
for x in range(1,factorial+1):
    factorial_result*=x
print(factorial_result)
#pattern
for x in range(1,6):
    for y in range(1,x+1):
        print("e", end="")
    print()
#largest_numvber
largest_number="4354354398"
largest_number_result=0
for x in largest_number:
    if int(x)>largest_number_result:
        largest_number_result=int(x)
print(largest_number_result)
#replace series of words
years_normal=["jan 2023", "dec 2023", "kee 2025"]
updated_years_normal=[]
for year_normal in years_normal:
    if year_normal.endswith("2023"):
        updated=year_normal.replace("2023","2025")
        updated_years_normal.append(updated)
    else:
        updated_years_normal.append(year_normal)
print(updated_years_normal)
updated_list=["keerthivasan A", "Harshwadha s", "Anu s"]
updated_list_final=[updated_lists.replace("s", "K") if updated_lists.endswith("s") else updated_lists for updated_lists in updated_list]
print(updated_list_final)
#count how many times each letter is present
count_letter="77879473578435"
count_letter_final={}
for x in count_letter:
    if x not in count_letter_final:
        count_letter_final[x]=0
    count_letter_final[x]+=1
print(count_letter_final)
#addition of values
def addition_of_values(addition):
    final_value_of_addition=0
    for user,value in addition.items():
            final_value_of_addition+=addition[user]
    return round(final_value_of_addition, 2)
print(addition_of_values({"EndUser1": 2.753, "EndUser2": 4, "EndUser3": 1, "EndUser4": 3, "EndUser5": 6, "EndUser6": 8}))
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
time=0.0
for key, value in FileServer.items():
     time+=value
print(time)
#assining each value with key
def list_full_names(first_last):
    full_name=[]
    for first,lasts in first_last.items():
        for last in lasts:
            combine=first+ " "+ last
            full_name.append(combine)
    return(full_name)
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
#changing key to value and value to key
def invert_resource_dict(input_resource):
    invert_resource_dict_output={}
    for system, device in input_resource.items():
        for devices in device:
            if devices in invert_resource_dict_output:
                invert_resource_dict_output[devices].append(system)
            else:
                invert_resource_dict_output[devices]=[system]
    return invert_resource_dict_output
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
#entering our input to the output
def word_place(input_replace):
    name=""
    year=""
    input_replace2=input_replace.split()
    for input_replace1 in input_replace2:
        if input_replace1.isalpha():
            name+=input_replace1+" "
        else:
            year=input_replace1
    name=name.strip()
    return ("{} who is famous among peole in {}".format(name,year))
print(word_place("Jacki sherrif was a great 1989"))
#extend and sorting
def year_add(year_90, year_20):
    year_20.sort()
    year_90.extend(year_20)
    #return year_90
year_90=[1997,1998,1999]
year_20=[2000,2003,2002,2001]
#print(year_add(year_90, year_20))
year_add(year_90, year_20)
print(year_90)
#Assining multiple value to our format
def network(key_value):
    key1=""
    for keyy, value1 in key_value.items():
        key1+="{} is the name and the pord id is {}".format(keyy, value1) + "\n"
    return key1
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))
#squaer of numbers in both list and normal
square_number_list=[n*n for n in range(1,11)]
print(square_number_list)
for square_number_normal in range(1,11):
    square_number_list_ooutput= square_number_normal*square_number_normal
    print(square_number_list_ooutput)
#Even numbers between 1 to 20
even_numbers_list=[n for n in range(1,21) if n%2==0]
print(even_numbers_list)
for even_number_normal in range(1,21):
    if even_number_normal%2==0:
        print(even_number_normal)
#condtion list
conditon_list=[f"{num} even" if num%2==0 else f"{num} odd" for num in range(0,11) ]
print(conditon_list)
for value_typing in range(0,11):
    if value_typing%2==0:
        print(value_typing, "even")
    else:
    #elif value_typing%3==0:
        print(value_typing, "odd")
#making multiple list into single list
flatten=[[1, 2], [3, 4], [5, 6]] 
flatten_list=[f2 for f1 in flatten for f2 in f1 ]
print(flatten_list)
flatten_normal=[[1, 2], [3, 4], [5, 6]]
f22=[]
for fog in flatten_normal:
    for f23 in fog:
        f22.append(f23)
print(f22) 
#common elements
lists1=[1, 2, 3, 4] 
lists2=[3, 4, 5, 6]
common_list=[lists for lists in lists2 if lists in lists1]
print(common_list)
lists3=[1, 2, 3, 4] 
lists4=[3, 4, 5, 6]
lu=[]
for listu in lists3:
    if listu in lists4:
        print(listu)
        lu.append(listu)
print(lu)
#reverse word
list_reverse= ["hello", "world", "python"]
reversing=[lists_reverse[::-1] for lists_reverse in list_reverse]
reversing1=[list_reverse[::-1] ]
print(reversing)
print(reversing1)
list_reverse1= ["hello", "world", "python"]
reversing_2=[]
for listt in list_reverse1:
    reversing_2.append(listt[::-1])
print(reversing_2)
#filter and transform
filter1=[5,10,11,15,20,25]
filter_list=[add+10 for add in filter1 if add%5==0 ]
print(filter_list)
filter2=[5,10,11,15,20,25]
for adding in filter2:
    if adding%5==0:
        final_adding=adding+10
        print(final_adding)
#Dictionary task
#word count
def word_count(fruits):
    count_dictionary={}
    fruits_split=fruits.split()
    for fruit in fruits_split:
        if fruit not in count_dictionary:
            count_dictionary[fruit]=0
        count_dictionary[fruit]+=1
    return count_dictionary
print(word_count("apple banana apple orange banana apple"))
input_fruits="apple banana apple orange banana apple"
assign_dictionary={}
input_fruits_split=input_fruits.split()
for input_split in input_fruits_split:
    if input_split in assign_dictionary:
        assign_dictionary[input_split]+=1
    else:
        assign_dictionary[input_split]=1
print(assign_dictionary)
#square dictionary
def square_dictionary(square_value):
    square_dictionary_result={}
    for square in range(1,square_value):
        square_dictionary_result[square]=square*square
    return square_dictionary_result
print (square_dictionary(10))
#inverted_dictionary
def inverted_dictionary(assigned_values):
    inverted_dictionary_result={}
    for assign, values in assigned_values.items():
        inverted_dictionary_result[values]=assign
    return inverted_dictionary_result
print(inverted_dictionary({"a": 1, "b": 2, "c": 3}))
#Filter Dictionary
def Filter_Dictionary(values_above):
    Filter_Dictionary_result={}
    for assign, assign_value in values_above.items():
        if assign_value>5:
            Filter_Dictionary_result[assign]=assign_value
    return Filter_Dictionary_result
print(Filter_Dictionary({"a": 5, "b": 15, "c": 8, "d": 20}))
#Group by First Letter
def Group_by_First_Letter(initial_assignment):
    Group_by_First_Letter_result={}
    for first_iterate in initial_assignment:
        first_letter=first_iterate[0]
        if first_letter not in Group_by_First_Letter_result:
            Group_by_First_Letter_result[first_letter]=[]
        Group_by_First_Letter_result[first_letter].append(first_iterate)
    return Group_by_First_Letter_result
print(Group_by_First_Letter(["apple", "banana", "apricot", "blueberry", "cherry"]))
#Nested_dictionary
names = ["Alice", "Bob"]
details = [{"age": 25, "city": "NY", "State": "TN"}, {"age": 30, "city": "LA"}]
# I am giving format through : and then normal for loop which is assigning values like name is names and
#details is detail zip is used to map
comprehension={name: detail for name,detail in zip(names, details)}
print(comprehension)
#character_frequency
def character_frequency(separate):
    character_frequency_store={}
    for sepa in separate:
        if sepa!=" ":
            if sepa in character_frequency_store:
                character_frequency_store[sepa]+=1
            else:
                character_frequency_store[sepa]=1
    return character_frequency_store
print(character_frequency("hello worlf"))
#Merge_Dictionaries    
a={"a": 10, "b": 20}
b={"b": 5, "c": 15}
copy_a=a.copy()
for ke,va in b.items():
    if ke in copy_a:
        copy_a[ke]+=va
    else:
        copy_a[ke]=va
print(copy_a)
#1.	Dictionary Comprehension: Create a dictionary where keys are numbers from 1 to 10 
# and values are "Even" or "Odd" based on the number.
list_comprehension={num: "even" if num%2==0 else "odd" for num in range(1,11)}
list_comprehension1=[{num: "even"} if num%2==0 else {num: "odd"} for num in range(1,11)]
list_comprehension2=[f"{num}: even" if num%2==0 else f"{num}:odd" for num in range(1,11)]
print(list_comprehension)
print(list_comprehension1)
print(list_comprehension2)
#Word_length
Input= ["python", "java", "c++"]
word_store={}
for length_calculator in Input:
    length_function=len(length_calculator)
    word_store[length_calculator]=length_function
print(word_store)
#flatten_dictionary_values
make_it_single={"a": [1, 2], "b": [3, 4, 5], "c": [5]}
make_it_single_output=[]
for make,maker in make_it_single.items():
        make_it_single_output.extend(maker)
print(make_it_single_output)
make_it_single1 = {"a": [1, 2], "b": [3, 4, 5 ], "c": [5]}
make_it_single_output1 = set()
for make1, maker1 in make_it_single1.items():
    make_it_single_output1.update(maker1)  # Using update to add values to the set
print(make_it_single_output1)
# Flatten a dictionary where values are lists into a single list
input_dict = {"a": [1, 2], "b": [3, 4, 5], "c": [5]}
flattened_list = [value for values in input_dict.values() for value in values]
print(flattened_list)
# Output: [1, 2, 3, 4, 5]
flatten_list1=[[1, 2], [3, 4], [5, 6]] 
flatten_list_result=[values for value in flatten_list1 for values in value]
print(flatten_list_result)
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
honeycrisp = Apple("red", "sweet")
print(honeycrisp)






