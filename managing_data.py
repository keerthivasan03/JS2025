"""def time_onversion(hours,minute,second):
    return hours*3600+minute*60+second
print("Welcomt to time calculator")

cont="y"
while (cont.lower()=="y"):
   hours= int(input("Enter hours:"))
   minute= int(input("Enter minutes:"))
   second= int(input("Enter Second:"))
   print("That's {} second".format(time_onversion(hours,minute,second)))
   print()
   cont=input("Enter the y to continue")
print("Bye")

mm=(input("Enter a number"))
print(mm)
print(type(mm))
print(eval(mm))

import re
def show_time_of_pid(line):
  pattern = r"^(\w+ \d+ \d+:\d+:\d+) .*?\[(\d+)\](?:.*?USER \((\w+)\))?"
  #pattern= r"^(\w+ \d+ \d+:\d+:\d+) .*?\[(\d+)\](?:.*?USER \(([^)]+)\))?"
  result = re.search(pattern, line)
  #return f"{result.group(1)} pid:{result.group(2)}"
  if not  result:
   return "No data type found"  
  date=result.group(1)
  number=result.group(2)
  username=result.group(3) if result.group(3) else None
  if username: 
    return f"{date} pid:{number} username:{username}"
  else:
    return f"{date} pid:{number}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
"""



import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

usernames1 = {}
name1 = ["good_user","bad user"]
for x in name1:
    
    usernames1[x] = usernames1.get(x, 0) + 1
    print(usernames1)
    usernames1[x] = usernames1.get(x, 0) + 1
    print(usernames1)

usernames2 = {}
name2 = ["good_user","bad user"]
for x in name2:
    
    usernames2[x] = usernames2.get(x, 0) + 1
    usernames2[x] = usernames2.get(x, 0) + 1
print(usernames2)

