import sys

# Read command line arguments and convert to a list of integers
arr = sys.argv[1].split(',')
my_numbers = [None]*len(arr)
for idx, arr_val in enumerate(arr):
    my_numbers[idx] = int(arr_val)

# Print
print(f'Before sorting {my_numbers}')

for i in range(len(my_numbers)):
    for j in range(i+1,len(my_numbers)):
        if my_numbers[i]>my_numbers[j]:
            my_numbers[i],my_numbers[j] = my_numbers[j],my_numbers[i]
# Print
print(f'After sorting {my_numbers}')





