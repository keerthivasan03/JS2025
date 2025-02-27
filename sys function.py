import sys
sys.argv=["Hello","World"]
if len(sys.argv) != 3:
    sys.exit("Error: Please provide exactly 2 arguments.")

print(f"Arguments received: {sys.argv[1]} and {sys.argv[2]}")

import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(f"Sum: {num1 + num2}")

