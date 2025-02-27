import re
log = "July 31 07:51:48 mycomputer bad_process[123455354]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

res=re.search(r"eerthi","jfkdseerthi")
print(res)
small=re.search(r"[pP]i[Cc]k","pickle")
print(small)
ign=re.search(r"wash", "Washing",re.IGNORECASE)
print(ign)
isor=re.search(r"kee|an","Keerthivasan anu ")
print(isor)
isor1=re.findall(r"kee|an","Keerthivasan anu ",re.IGNORECASE)
print(isor1)
ioo=re.search(r"py.*n", "python ")
print(ioo)
ioo1=re.search(r"py[a-z]*n", "python programming")
print(ioo1)
ioo1=re.search(r"p+r+", "python programming")
print(ioo1)
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome.com"))
print(re.search(r"\w*", "welcome my name"))
print(re.search(r"\w*", "welcome_my_name"))
print(re.search(r"A.*a", "Azerbaigan"))
print(re.search(r"^A.*a$", "Azerbaiga"))
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]*[.?!]$", text)
  return result != None
print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return print("{} {}".format(result[2], result[1]))
rearrange_name("Hopper, Grace M.")