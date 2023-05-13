# Exercise 1
str1 = input("Enter a word: ")
res = str1[len(str1)//2 - 2: len(str1)//2 + 1]
print("res = ", res)

# Exercise 2
s1 = input("Enter first word: ")
s2 = input("Enter second word: ")
res2 = s1[0: len(s1)//2] + s2 + s1[len(s1)//2: len(s1)] # first goes only from 0 < len//2, second time from len//2 < len
print("res = ", res2)
