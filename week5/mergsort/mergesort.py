def merge_Sort(unordered_arr):
    if len(unordered_arr) > 1:
        mid = len(unordered_arr) // 2
        l = unordered_arr[:mid]
        r = unordered_arr[mid:]

        
        merge_Sort(l)
        merge_Sort(r)
   
        a = 0
        b = 0  
        c = 0
        
        while a < len(l) and b < len(r):
            if l[a] < r[b]:
             
              unordered_arr[c] = l[a]
              
              a += 1
            else:
                unordered_arr[c] = r[b]
                b += 1

            c += 1

        while a < len(l):
            unordered_arr[c] = l[a]
            a += 1
            c += 1

        while b < len(r):
            unordered_arr[c]=r[b]
            b += 1
            c += 1

arr = [14, 46, 43, 27, 57, 41, 45, 21, 70]  
merge_Sort(arr)
print(arr)
