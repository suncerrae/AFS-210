# a = [1,62,38,4,45,6,7]

# def listValue(a):
#     newlist = []
#     minChar = a[1]
#     length = len(a)
#     counter = 0
#     for i in a:
#         i = int(i)
#         if i <  minChar:
#              minChar = i
#              newlist.append(i)
#              a.remove(i)
#              counter = counter + 1
#              if counter == length:
#                 return newlist
    
    

            
    
# print(listValue(list))


a = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

def sortList(a):
    for i in a:
        j = a.index(i)
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1
    return j

print(sortList(a))

