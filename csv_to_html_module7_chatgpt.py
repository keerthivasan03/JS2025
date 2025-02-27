import csv
import re
import operator
import os

# ✅ Check if file exists
print(os.path.exists("C:\\Users\\keerthivasan.a\\syslog.log"))

# ✅ Initialize dictionaries
per_user = {}
error = {}

# ✅ Read syslog file
with open("C:\\Users\\keerthivasan.a\\syslog.log", "r", newline="") as extract:
    for line in extract:
        # ✅ Fixed regex to capture only ERROR messages
        searching = r"ticky: (ERROR): (.+) \(([\w.]+)\)"
        capture = re.search(searching, line)

        if not capture:  # ✅ Skip if no match
            continue

        code, error_message, user = capture.groups()

        # ✅ Count errors
        error[error_message] = error.get(error_message, 0) + 1

        # ✅ Initialize user dictionary if new
        if user not in per_user:
            per_user[user] = {"INFO": 0, "ERROR": 0}

        # ✅ Increment ERROR counts
        per_user[user]["ERROR"] += 1

# ✅ Read INFO logs separately to track INFO counts correctly
with open("C:\\Users\\keerthivasan.a\\syslog.log", "r", newline="") as extract:
    for line in extract:
        searching_info = r"ticky: (INFO): .+ \(([\w.]+)\)"
        capture_info = re.search(searching_info, line)

        if capture_info:
            user = capture_info.group(1)
            if user not in per_user:
                per_user[user] = {"INFO": 0, "ERROR": 0}
            per_user[user]["INFO"] += 1  # ✅ Increment INFO count

# ✅ Sort error messages by count (descending)
error_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

# ✅ Sort user statistics by username (ascending)
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

# ✅ Write error messages CSV
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "w", newline="") as error_write:
    error_generate = csv.writer(error_write)
    error_generate.writerow(["Error", "Count"])  # ✅ Add header
    for key, value in error_list:
        error_generate.writerow([key, value])

# ✅ Read and print error messages
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "r") as error_read:
    error_reader = csv.DictReader(error_read)
    for row in error_reader:
        print("Error: {}, Count: {}".format(row["Error"].strip(), row["Count"].strip()))  # ✅ Fixed

# ✅ Write user statistics CSV
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "w", newline="") as user_write:
    user_generate = csv.writer(user_write)
    user_generate.writerow(["User", "Info", "Error"])  # ✅ Add header
    for key, value in per_user_list:
        user_generate.writerow([key, value["INFO"], value["ERROR"]])

# ✅ Read and print user statistics
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "r") as user_read:
    user_reader = csv.DictReader(user_read)
    for row in user_reader:
        print("User: {}, Info: {}, Error: {}".format(row["User"].strip(), row["Info"].strip(), row["Error"].strip()))  # ✅ Fixed
