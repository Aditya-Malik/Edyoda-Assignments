# 1. Print all sub arrays for a given array. Ex - if array is [2, 7, 5], Output will be: [2] [2, 7] [2, 7, 5] [7] [7, 5] [5].
def subArray(array):
    n=len(array)
    for i in range(0,n):
        for j in range(i,n):
            k=i
            sub_array=[]
            while k<=j:
                sub_array.append(array[k])
                k+=1
            if len(sub_array)>0:
                print(sub_array)

subArray([2,7,5])