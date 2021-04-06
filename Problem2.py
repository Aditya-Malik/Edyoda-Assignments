#2. Rotate an array by one. Ex - if array is [1, 4, 6, 8, 7] Output will be [7, 1, 4, 6, 8]
import array as ar
input=input().split(" ")
ar_input=[]
for number in input:
    ar_input.append(int(number))
arr1=ar.array("i",ar_input)
arr2=ar.array("i",[])
arr2.append(arr1[-1])
for index,element in enumerate(arr1):
    if element not in arr2:
        arr2.append(element)
list=[]
for index,element in enumerate(arr2):
    list.append(element)
print(list)