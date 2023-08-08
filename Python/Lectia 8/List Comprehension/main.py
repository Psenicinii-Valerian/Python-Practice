# list comprehension = list generator
# list generator != generator
# ls_name = [1. (elementele listului) 2. (for si crearea elementelor + colectia) 3. if]
                                                        # LISTS
# squares = [x ** 2 for x in range(1, 10)]
# print(squares)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
#
# word = "Hello"
# characters = [ch for ch in word]
# print(characters)
#
# strings = ["Hello", " ", "Python", " ", "Word"]
# lenghts = [len(string) for string in strings if string.strip() != '']
# print(lenghts)
#
# cars = ['Accord', 'Skyline', 'Supra']
# colors = ['White', 'Blue', 'Purple']
#
# combinations = [(car, color) for car in cars for color in colors]
# print(combinations)
#
# nums = [x**2 for x in range(1,12) if x%2 == 0 and x%4 != 0]
# print(nums)

                                                        # SETS
# m_set = {i for i in range (1, 7)}
# print(type(m_set))
# print(m_set)
#
# setikk = set()
# for i in range(1, 7):
#     setikk.add(i)
# print(setikk)
#
# m_set2 = {i for i in [0, 1, 1, 1, 2, 3, 4, 0, 4, 5]}
# print(m_set2)
#
# setik = {i for i in ["Hello", "zdarova", "zdarova",  "ola", "ola", "salut", "salut", "salut", "salut", "paka"]}
# print(setik)
#
# setik2 = {i for i in "Abracadabra"}
# print(setik2)
#
# setik3 = {i for i in ["Hello", "zdarova", "zdarova",  "ola", "ola", "salut", "salut", "salut", "salut", "paka"] if len(i) < 5}
# print(setik3)
#
# setik4 = {i+j for i in 'abc' for j in 'def'}
# listik = [[i+j] for i in 'abc' for j in 'def']
# print(setik4)
# print(listik)

                                                        # DICTIONARIES
a = {i: i**2 for i in range(1, 11)}
print(a)

# a2 = {}
# for i in range(1, 11):
#     a2[i] = i**2
# print(a2)

a2 = {word: len(word) for word in ['konichiwa', 'zdarova', 'salut']}
print(type(a2))

games = {
    "League of Legends": "140",
    "Dota 2": "123",
    "Valorant": "20"
}

new_games = {key.title(): int(value) for key, value in games.items()}
print(new_games)

# new_game = {}
# for key, value in games.items():
#     new_game[key.title()] = int(value)
# print(new_game)

users = [
    [0, "Skolinik_98", "avatartop"],
    [1, "hacker_Pr0", "dkfsajfsaj##!@123"],
    [2, "aNiMe_LovER228", "IuBeScMIvina12"],
    [3, "kimateru", "wifiroutertelefon"],
    [87, "Skolinik_98", "avatartop"],
]

print(users[3][1]) # will print kimateru
new_users = {user[0]: [user[1], user[2]] for user in users}
for key, value in new_users.items():
    print(f"{key}: {value}")
