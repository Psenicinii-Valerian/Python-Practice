"""
Multiple line comments
123
docs
"""

# + - * / // % **
# // - floor division

# info = ["Psenicinii", "Valerian", "Chisinau", "Oslo", 19];
# print(info)

"""
my_info = {
   "name": "Valerian",
   "surname": "Psenicinii",
   "origin city": "Chisinau",
   "city I'd love to live in": "Oslo",
   "age": 20
}

for key, value in my_info.items():
    print(f"{key} : {value}")

num_to_pow = int(input("Enter a number you want to raise to a power: "))
num_to_pow **= 2
print(num_to_pow)
"""

           # String data type
# s = "Hello"
# s1 = s[0] #first symbol
# s2 = s[-1] #last symbol
# print("ur string has: ", len(s), "characters")
#
# #len(string) - number of symbol
#
# if 'He' in s:
#     print(f"Found letter H in {s}!")
# else:
#     print(f"Didn't find letter H in {s}!")
# #if .. in .. - allows us to find anything inside of something
#
#           # String cutting
# s1 = "Abracadabra is magic"
# res = s1[0:11:2]    # prints the characters of s1 string from 0 to 11 with the step 2 (0, 2, 4, .., 10)
# print(res)
# res = s1[::2]   # prints the characters of s1 string starting from 0 with step 2 (0, 2, 4, ..)
# print(res)
# res = s1[10:0:-1]   # prints the string backwards (reversed)
# print(res)

            # String methods
# string are not mutable !!!
# string.upper() - transforms strings to upper case
# string.lower() - transforms strings to lower case
# string.count('value', [start], [end]) - counts how many times finds value
# string.find('value') - finds the index of value from left
# string.rfind('value') - finds the index of value from right
# string.replace('old', 'new') - replace one substring with another
# string.isdigit() - checks if string is a number
# string.isalpha() - checks if string is a text
# string.split('value') - splits a string (by the delimiter 'value') in a list (array)
# s = "".join('string') - joins list elements into string (with each list elem being separated by " " - space)

# s = "Hello Pyth Pon"
# print(s)
# print(s.lower())
# print(s.count('o'))
# print(s.find('P'))
# print(s.rfind('P'))
# print(s.replace('o', '!'))
# print(s.isdigit())
# print(s.isalpha())
# print(s.split(" "))
# print("".join(s))

