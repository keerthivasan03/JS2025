#1
input_str = "Keerthi Vasanooo"
vowels = "AEIOUaeiou"

# Extract vowels and reverse them
vowel_chars = [ch for ch in input_str if ch in vowels]
vowel_chars.reverse()
print(vowel_chars)

# Build final string with reversed vowels
result = ""
vowel_index = 0
for ch in input_str:
    if ch in vowels:
        result += vowel_chars[vowel_index]
        vowel_index += 1
    else:
        result += ch

print("Original String:", input_str)
print("After Reversing Vowels:", result)

#2
input_str = "A1B2C3D4"
digits = [ch for ch in input_str if ch.isdigit()]
digits.reverse()

result = ""
digit_index = 0
for ch in input_str:
    if ch.isdigit():
        result += digits[digit_index]
        digit_index += 1
    else:
        result += ch

print("Reversed digits:", result)

#3
input_str = "a@b#c1d$e"
letters = [ch for ch in input_str if ch.isalpha()]
letters.reverse()

res = ""
i = 0
for ch in input_str:
    if ch.isalpha():
        res += letters[i]
        i += 1
    else:
        res += ch

print("Only letters reversed:", res)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # From parent class
d.bark()   # From child class
