# 1 ---------- COUNT THE POSITIVE NUMBER FROM THERE ------------------
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count = 0
#
#
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
#
# print(f"Number of positives are {positive_number_count}")

# 2 ---------- Sum of even number ------------------
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_of_even_num = 0
#
# for num in numbers:
#     if num % 2:
#         sum_of_even_num += num
#
# print(f"Sum of even numbers are {sum_of_even_num}")


# 2 ---------- Multiplication Table Printer ------------------
#
# number = 3
#
# for i in range(1,11):
#     if i == 5:
#         continue
#
#     print(number ," * ",i," = ",i * number)

# 3 ---------- Reverse String ------------------
#
# my_world = "hello world"
# rev_string = ""
#
# for char in my_world:
#     rev_string = char + rev_string
#
# print(rev_string)

# 4 ---------- find first none repeated character ------------------

# my_string = "hello world"
#
# for char in my_string:
#     if my_string.count(char) <= 1:
#         print(char)
#         break


# 4 ---------- Factorial Calculator ------------------
#
# num = 10
# facto = 1
#
# while num >= 1:
#     facto *= num
#     num -= 1
#
# print(facto)

# 4 ---------- Input validation ------------------


# while True:
#     num = int(input("Enter number between 1 - 10:- "))
#     print(num)
#
#     if 11 > num > 0:
#         break
#     else:
#         print("Invalid Number! Try again")
#


# 4 ---------- Prime Number checker ------------------

number = 6

for i in range(2,number):
    if number % i == 0:
        print("Number is not prime number")
        break
