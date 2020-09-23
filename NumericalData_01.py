heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 173, 175, 178, 183, 193, 178, 188, 192, 185, 182, 180]

"""If we want to know how many heights are grater than 188cm, we could iterate through the list, compare each element against 188cm and increase count by 1 as the careteria met"""

count = 0
for height in heights:
    if height > 188:
        count += 1
print(count)

"""No matter the formate of the data, the first step in data science is to transform it into array of numbers"""