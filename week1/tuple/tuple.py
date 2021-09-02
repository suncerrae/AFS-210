from collections import defaultdict
classes = (
    ('VII', 1),
    ('V', 1),
    ('V', 2),
    ('VI', 1),
    ('VI', 2),
    ('VI', 3),
)

rollno = defaultdict(list)

for cname, id in classes:
    rollno[cname].append(id)

print(rollno)