from collections import defaultdict
romanLetters = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

rollNumber = defaultdict(list)

for letter, num in romanLetters:
    print("letter", letter)
    print("num", num)
    rollNumber[letter].append(num)

print(rollNumber)