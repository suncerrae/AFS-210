darray = [1,2,3,4,5,6,7]


def balance(arr):
    treeOrder =[]

    def findingRoot(array):
        finding0Root = array[(len(array)//2)]
        print(finding0Root)
        treeOrder.append(finding0Root)
        array.remove(finding0Root)
        
    findingRoot(arr)

    rootindex = (len(arr)//2)
    print(treeOrder)
    
    left = arr[0:rootindex]
    print(arr[0:rootindex])
    while len(left) > 2:
        findingRoot(left)
        print(left)
        

        # for num in len(left):
        #     left.remove(num)
    treeOrder += left
    right = arr[rootindex:]
    print(arr[rootindex:])

    while len(right) > 2:
        findingRoot(right)
        print(right)
        

        # for num in len(right):
        #     right.remove(num)
    treeOrder += right
    return treeOrder

    

print(balance(darray))