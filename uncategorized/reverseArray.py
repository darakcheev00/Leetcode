arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7,8]

def reverseArr(arr):
    i,j = 0,len(arr)-1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

    return arr

print(reverseArr(arr1))
print(reverseArr(arr2))