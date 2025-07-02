list_arr = ["Hello", "World", "Python", "is", "awesome"]

print(list_arr[0:4])
print(list_arr[-1])



list_arr[0] = "Hi"
list_arr[0:2] = ["Hi", "Universe"]
list_arr[0:0] = ["Hello/"]

list_arr.append("!")
list_arr.insert(0, "!")

list_arr_copy = list_arr.copy() # If you does not use use copy() method, it will be a reference to the original list and any changes made to the copy will affect the original list.

squared_number = [num ** 2 for num in range(1, 11)]

print(squared_number)


# value = range(1, 11)
#
# for number in value:
#     print(number)

for items in enumerate(list_arr):
    print(items) # This will return a tuple with the index and the value of the item in the list

print(list(range(0,11,2)))


print(list_arr)