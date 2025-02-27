import csv

file_path = "C:\\Users\\keerthivasan.a\\user_emails_1.csv"

# Use a comma as the delimiter
csv.register_dialect("CustomDialect", delimiter=",", quotechar='"', strict=False, skipinitialspace=True)

# Data to append
data = [{"Name": "Keerthivasan", "Email": "kkk@gmail.com"}]
keys = ["Name", "Email"]

# Open the file in append mode ('a') to avoid overwriting
with open(file_path, "a", newline='') as write_file:
    writer = csv.DictWriter(write_file, fieldnames=keys, dialect="CustomDialect")
    
    # Write header only if file is empty
    write_file.seek(0)
    if write_file.tell() == 0:
        writer.writeheader()
    
    # Append new data
    writer.writerows(data)

print("Data appended successfully.")
