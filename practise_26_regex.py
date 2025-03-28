import re
def regex(text):
    find=r"^[A-Z][0-9a-z\s].*[!.?]$"
    fine=re.search(find, text)
    return fine!=None
print(regex("I 9 eiore?"))
print(regex("I "))
print(regex("I love python"))
def check_sentence(text):
    reg=r"[a-zA-a\s].*"
    update=re.search(reg,text)
    return update!= None
print(check_sentence("Is ")) # True
print(re.search("Aa*","Aaaaaah"))
print(re.search("Aa.*","Aaaaaah"))
def sentence1(text):
    reg=r"[a-zA-Z\s].*"
    final=re.search(reg,text)
    return final!= None
print(sentence1("Msyz name is blah blah"))
print(re.search(r"[a-zA-Z]{5}","My name is Keert")) #search object which is having 5 character
print(re.findall(r"[a-zA-Z]{5}","My names is Keerthi")) #search all string which is having 5 character
print(re.findall(r"\b[a-zA-Z]{5}\b","My names is Keerthi")) #search all character which exactly match 5character between A-Za-z
print(re.findall(r"[a-zA-Z]\w{4,10}","My names is Keerthi"))#\w covers any letter between a-z0-9!space and the words match between 4-10
print(re.findall(r"[a-zA-Z]\w{,4}","My name is Keerthi"))#0-4
print(re.findall(r"[Kk]\w{,99}","My name is Keerthi"))#in Kk any word match between 0-99
def log(text):
    reg=r"\{(\d+)\}"
    fial=re.findall(reg,text)
    return fial
print(log("July 31 07:51:48 mycomputer bad_process{12345}: ERROR {1211} Performing package upgrade"))
def ff(text):
    reg=r"\[([\w+|\d+]{4,6})\]"
    fil=re.findall(reg,text)
    return fil
print(ff("July 31 07:51:48 mycomputer bad_process[dafdsf]: ERROR [1211] Performing package upgrade"))
def extract_pid(text):
    reg=r"\[([\d+]{5})\]:\s([A-Z]+)"
    #reg=r"\[(\d+)\]: ([A-Z]+)"
    dip=re.search(reg,text)
    if dip is None:
        return None
    return "{} {}".format(dip[2], dip[1])
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
def split(text):
    reg=r"[.:,!\s]"
    fial=re.split(reg,text)
    return fial
print(split("My name is Keerthivasan. I am From:Cheyyar, My Native is great! It is wow!"))
def sub(text):
    ss=r"[\w\.]+@[\w\.]+"
    fial=re.sub(ss, "XXXXX", text)
    return fial
print(sub("Received an email for keeerthivasan.a@protivitiglobal.in"))
def sub(kkk):
    reg=r"\(?([\d]{3})\)?[-\s]?([\d]{3})-([\d]{4})"
    fial=re.sub(reg,"********",kkk)
    return fial
print(sub("My phone numbers are 987-654-3210 and (123) 456-7890."))
def swap(text):
    reg=r"([\w]+), ([\w\s]+)"
    final=re.sub(reg,r"\2 \1",text)
    return final
print(swap("vasan, keerthi A"))
def multi_vowel_words(text):
    reg=r"\w+[aeiouAEIOU]{3}\w+"
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
def kk(text):
    #reg=r"\b\w+[aeiouAEIOU][^aeiouAEIOU$]{3,}\w+\b"
    #reg=r"\b\w*(?:[aeiouAEIOU][^aeiouAEIOU]*){3,}\w*\b"
    reg=r"\b\w*(?:[aeiouAEIOU][^aeiouAEIOU]*){3,}\w*\b"
    fina=re.findall(reg,text)
    return fina
print(kk("Obviously, great person ever keerthoi seen in my life, beautiful beautiful"))
def code_regex(text):
    first=r"\w+"
    first_regex=re.findall(first,text)
    result=[]
    print(first_regex)
    for second in first_regex:
        reg=r"[AEIOUaeiou]"
        new=re.findall(reg,second)
        print(new)
        if len(new)>=3:
            result.append(second)
    return result            
print(code_regex("The Rambunctious, childern had to sit quietly to enjoy their delicious foodsa keerthi"))
import logging
logging.debug("Tihs is debug message")


# Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO,force=True)

# Get a logger object
log = logging.getLogger(__name__)
logging.debug("Tihs is debug message")



# Start the log file
log.info("Hello world")