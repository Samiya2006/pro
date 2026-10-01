#write a program to find the largest number in an array
def large(arr):
    large =arr[0]
    for i in arr:
        if i>large:
            large =i
    return large
arr = [10, 25, 7, 45, 32]
result = large(arr)
print("Largest number is :" , result)