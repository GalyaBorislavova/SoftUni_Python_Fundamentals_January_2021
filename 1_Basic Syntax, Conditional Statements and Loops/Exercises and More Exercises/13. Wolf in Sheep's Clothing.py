str1 = input()

str1 = list(str1.split(", "))

for n in range(len(str1)):
    if str1[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if str1[n] == "wolf":
        wolf_position = n
        sheep_position = len(str1) - (n + 1)
        print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
        break