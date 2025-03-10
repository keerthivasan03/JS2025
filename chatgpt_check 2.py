import csv
from pprint import pprint
#Git check
def convert_employee_data(file_path):
    with open(file_path, "r") as dictionary:
        # Register CSV dialect with space as delimiter
        csv.register_dialect("Employee", delimiter=" ")
        convert_dic = csv.DictReader(dictionary, dialect="Employee")
        add_dic = [data for data in convert_dic]
        return add_dic

def filter_employees(employee_data, age_threshold=25):
    # Filter employees older than age_threshold
    filtered = [emp for emp in employee_data if int(emp['Age']) > age_threshold]
    return filtered

def write_filtered_data(filtered_data, output_file):
    # Write filtered data to new CSV
    if not filtered_data:
        print("No data to write.")
        return
    
    fieldnames = filtered_data[0].keys()

    with open(output_file, "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)
    print(f"Filtered data written to {output_file}")

# --- Running the Code ---
file_path = "employee_data.csv"  # Replace with your input CSV file path
output_file = "filtered_employee_data.csv"

# Step 1: Read employee data
employee_data = convert_employee_data(file_path)
print("Original Employee Data:")
pprint(employee_data)

# Step 2: Filter employees (e.g., Age > 25)
filtered_employees = filter_employees(employee_data, age_threshold=25)
print("\nFiltered Employees (Age > 25):")
pprint(filtered_employees)

# Step 3: Write filtered data to a new CSV
write_filtered_data(filtered_employees, output_file)

