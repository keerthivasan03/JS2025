#Regex
#1
import re
def regex(text):
    find=r"^[A-Z][0-9a-z\s].*[!?]$" # .* Matches any number of characters (except newlines) after the second character
    final=re.search(find,text)
    return final != None
print(regex("I 9 eiore?"))
print(regex("I "))
print(regex("I love python"))
#2
def check_sentence(learn1):
    logs=r"^[A-Za-z\s].*$"
    final=re.search(logs,learn1)
    return final 
print(check_sentence("Is ")) # True
#3
print(re.search("Aa*","Aaaaah"))
print(re.search("Aa.*","Aaaaah"))
#4
def sentence1(text):
    logs=r"^[A-Za-z\s].*"
    final=re.search(logs,text)
    return final !=None
print(sentence1("Msyz name is blah blah"))
#5
print(re.search(r"[a-zA-Z]{5}","My name is Keert")) #search object which is having 5 character
print(re.findall(r"[a-zA-Z]{5}","My names is Keerthi")) #search all string which is having 5 character
print(re.findall(r"\b[a-zA-Z]{5}\b","My names is Keerthi")) #search all character which exactly match 5character between A-Za-z
print(re.findall(r"[a-zA-Z]\w{4,10}","My names is Keerthi"))#\w covers any letter between a-z0-9!space and the words match between 4-10
print(re.findall(r"[a-zA-Z]\w{,4}","My name is Keerthi"))#0-4
print(re.findall(r"[Kk]\w{,99}","My name is Keerthi"))#in Kk any word match between 0-99
#6
def log(text):
    #reg=r"\b[0-9]{4,5}\b" #match 0-9 with min 4 to 5
    reg=r"\{(\d+)\}" #match digits from 0-9 and + indicates increment if {} is with [] then we need to use it as \[\]
    final=re.findall(reg,text)
    return final
print(log("July 31 07:51:48 mycomputer bad_process{12345}: ERROR {1211} Performing package upgrade"))
#7
def ff(text):
    #reg=r"\[([\w+|\d+]{4,6})\]"
    reg=r"\[(\w+|\d+)\]" # either match string or numerical
    final=re.findall(reg,text)
    return final
print(ff("July 31 07:51:48 mycomputer bad_process[dafdsf]: ERROR [1211] Performing package upgrade"))
#8
def extract_pid(text):
    red=r"\[(\d+)\]: ([A-Z]+)" # match digits and followed by error I am adding + after [] is to match all the characters
    final=re.search(red,text)
    if final is None:
        return None
    return "{} ({})".format(final[2], final[1])
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
#9 split
def split(text):
    rege=r"[.,!:\s]"
    final=re.split(rege,text)
    return final
print(split("My name is Keerthivasan. I am From:Cheyyar, My Native is great! It is wow!"))
#10 sub\
def sub(text):
    reg=r"[\w\.]+@[\w\.]+"
    final=re.sub(reg,"Mail-id",text)
    return final
print(sub("Received an email for keeerthivasan.a@protivitiglobal.in"))
#11 sub 2
def sub2(text):
    reg=r"\(?\d{3}\)?[-\s]?(\d{3})-(\d{4})" #using ? to show that character may or may not present since we are having () in one number and not in another number
    final=re.sub(reg,"*********",text)
    return final
print(sub2("My phone numbers are 987-654-3210 and (123) 456-7890."))
#13 name swap sub
def swap(text):
    reg=r"([\w]+), ([\w\s]+)"
    final=re.sub(reg,r"\2 \1",text)
    return final
print(swap("vasan, keerthi A"))
#14 sub
def sub2(text):
    reg=r"(\d{3})-(\d{4})-(\d{4,5})"
    final=re.sub(reg,r"+1-\1-\2-\3",text)
    return final
print(sub2("My number is 123-2344-22922 and 231-3242-3423"))
#15 continuous words
def multi_vowel_words(text):
    reg=r"\w+[aeiouAEIOU]{3}\w+" # will check continuous words also with before and after words
    final=re.findall(reg,text)
    return final
print(multi_vowel_words("Life is beautiful beauotiful")) 
# ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']
print(multi_vowel_words("Hello world!")) 
#16 opp check
def parse_sentences(text):
    reg=r"\S+" #capital S states opp to s it will not take space 
    final=re.findall(reg,text)
    return final
print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']
#17 find specific pattern
def find_isbn(text):
    reg=r"\b\d{3}-\d-\d{2}-(\d{6})-\d\b"# will exactly match and give the below comment output
    #reg=r"\d{3}-\d-\d{2}-(\d{6})-\d"# will not exactly match and give the below 3rd comment as 098754 output
    final=re.search(reg,text)
    if final is None:
        return None
    return final[1]
print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank
#18 
def website(text):
    reg=r"https://([a-z\w\.]+)/([A-Za-z\w\.\/]+)"# we can even give the exact text we know and add our code
    final=re.search(reg,text)
    if final is None:
        return None
    return "{} {}".format(final[1],final[2])
print(website("https://pip.osourceglobal.com/PIP_PROTIVITI/Login.aspx")) #output: pip.osourceglobal.com
print(website("http://pip.osourceglobal.com/PIP_PROTIVITI/Login.aspx")) #output: none
#19
def kk(its_time1):
    #vowel1=re.findall(r"(\w*[aeiouAEIOU]{3}\w*)",its_time1) # match continuous vowel
    #vowel1 = re.findall(r"\b\w*(?:[aeiouAEIOU].*?){3}\w*\b", its_time1) #it should give if non consecutive is present but now not working
    vowel1 = re.findall(r"(\w*[aeiouAEIOU]{3}\w*.*?)",its_time1)
    return vowel1
print(kk("Obviously, great person ever keerthoi seen in my life, beautiful beautiful"))
#20 program
def code_regex(words):
    first_regex=re.findall(r"\w*",words)
    result=[]
    for second_Regex in first_regex:
        vowels=re.findall(r"[AEIOUaeiou]",second_Regex)
        if len(vowels)>=3:
            result.append(second_Regex)
    return result
print(code_regex("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa keerthi"))

List1 = [{'emp': 'John', 'dept no.': 12}, {'emp': 'Adam', 'dept no.': 5}]
for record in List1:
    output = []
    for key, value in record.items():
        output.append(f"{key} is {value}")
    print(" and ".join(output))

List1 = [{'emp': 'John', 'dept no.': 12}, [{'emp': 'Adam', 'dept no.': 5}]]

for record in List1:
    if isinstance(record, dict):
        output = []
        for key, value in record.items():
            output.append(f"{key} is {value}")
        print(" and ".join(output))
    elif isinstance(record, list):
        for subrecord in record:
            output = []
            for key, value in subrecord.items():
                output.append(f"{key} is {value}")
            print(" and ".join(output))


