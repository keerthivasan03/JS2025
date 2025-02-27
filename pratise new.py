import csv
import re
path="C:\\Users\\keerthivasan.a\\book_5.csv"
data={"Name":"Keerthivasan", "Another Name":"Anu", "Ann name":"Harishwadha"}
key=["Name","Another Name","Ann name"]
with open(path, "w", newline="") as path_writer:
    path_check=csv.DictWriter(path_writer,fieldnames=key)
    path_check.writeheader()
    path_check.writerow(data)
path1="C:\\Users\\keerthivasan.a\\book_6.csv"
data = [["Name", " Age", " City"],  # Extra spaces added intentionally
    ["Alice","34", " New York"],
    ["Bob", " 25", " Los Angeles"],
    ["Charlie", " 35", " San Francisco"]]
csv.register_dialect("Dia_name")
with open (path1,"w",newline="")as dd:
    path1_writer=csv.writer(dd,dialect="Dia_name",delimiter="|",strict=True,escapechar="'")
    path1_writer.writerows(data)
with open(path1,"r",newline="") as qq:
    path1_reader=csv.reader(qq,dialect="Dia_name")
    for row in path1_reader:
        print(row)
path1="C:\\Users\\keerthivasan.a\\book_1.csv"
with open(path1,"r",newline="") as qa:
    path1_header=csv.DictReader(qa)
    for row in path1_header:
        print ("{} is the name {} of the age {} of the city".format (row["name"], row["username"], row["department"]))

print(re.search("[Bb].rn","Burn"))
print(re.search("(\d+)","[64565465]"))
print(re.search("\w","Keerthi vasan"))
print(re.search("\w+","Keerthi_vasan"))
print(re.search("[kK]ee[a-z]","Keerthi_vasan"))
ioo1=re.search(r"ro", "python programming")
print(ioo1)
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]$", text)
  return result != None
print(check_sentence("Is ")) # True
def regex(ttt):
    res=re.search(r"^[A-Z][a-zA-Z0-9\s].*[.?!]$",ttt)
    return res!=None
print(regex("I 9 eiore?"))
print(regex("I "))
print(regex("I love python"))
print(re.search("Aa*","Aaaaah"))
print(re.search("Aa.*","Aaaaah"))
print(re.search(r"[a-z][A-Z\s].*$","Msyz name is blah blah"))
print(re.search(r"[a-zA-Z]{5}","My name is Keert"))
print(re.findall(r"[a-zA-Z]{5}","My names is Keerthi"))
print(re.findall(r"\b[a-zA-Z]{5}\b","My names is Keerthi"))
print(re.findall(r"[a-zA-Z]\w{4,10}","My names is Keerthi"))
print(re.findall(r"[a-zA-Z]\w{,4}","My name is Keerthi"))
print(re.findall(r"[Kk]\w{,99}","My name is Keerthi"))
log = "July 31 07:51:48 mycomputer bad_process{12345}: ERROR {1211} Performing package upgrade"
ss=re.search(r"\{(\d+)\}", log)
print(ss[1])
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR [1211] Performing package upgrade"
ss=re.search(r"\[(\d+)\]", log)
print(ss[1])
def ff(log):
    ss=re.search(r"\[(\d+)\]", log)
    if ss is None:
        return "sa"
    return ss
print(ff("July 31 07:51:48 mycomputer bad_process[dafdsf]: ERROR [1211] Performing package upgrade"))
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

print(re.split(r"[,.:!?]","My name is Keerthivasan. I am From:Cheyyar, My Native is great! It is wow!"))
print(re.split(r"([,.:!?])","My name is Keerthivasan. I am From:Cheyyar, My Native is great! It is wow!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "REDACTED", "Received an email for keeerthivasan.a@protivitiglobal.in"))

text = "My phone numbers are 987-654-3210 and (123) 456-7890."
masked_text = re.sub(r"\d{3}[-.) ]?\d{3}[-. ]?\d{4}", "REDACTED", text)
print(masked_text)

print(re.sub("[\w+\d_.]+@[\w+\d_.]+","Mine","My email ID is Keerthi1+223@gmail.com"))
print(re.sub(r"([\w .-]*),([\w .-]*)", r"\2,\1", "Keerthi,vasan"))
print(re.sub(r"(\d{3}-\d{4}-\d{3,7})",r"+1-\1","My number is 123-2344-22922 and 231-3242-3423"))
print(re.findall(r"\b\w*[aeiouAEOIU]{3,}\w*\b","beautiful"))
print(re.findall(r"\b\w*[aeiouAEIOU]{3,}\w*\b","Keerothi vaosain"))

def multi_vowel_words(text):
  pattern = r"\b\w*[aeiouAEIOU]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
def parse_sentences(sentence):
 pattern =r"\S+" #enter the regex pattern here
 result = re.findall(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']

def find_isbn(list):
  pattern = r"^\b\d{3}-\d-\d{2}-(\d{6})-\d\b$" #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return result[1] #return the correct capturing group


print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank