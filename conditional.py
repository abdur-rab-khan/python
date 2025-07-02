from datetime import datetime

# Question 01

# while True:
#     age = int(input("Enter your age Please: "))
#
#
#     if age == 0:
#         break
#
#     if age < 13:
#         print("Child")
#     elif age <= 19:
#         print("Teenager")
#     elif age <= 59:
#         print("Adult")
#     else:
#         print("Senior")

# ADULT_PRICE = 12
# CHILDREN_PRICE = 8
# WED_DISCOUNT = 2
# PRINT_STATEMENT = "Movies Ticket price is {}"
#
# while True:
#     age = input("Enter your age Please: ")
#     current_date = datetime.now()
#     current_day = current_date.strftime("%A")
#
#     if age.isdigit():
#         age = int(age)
#     else:
#         print("Please enter a valid number")
#         continue
#
#     if age == 0:
#         break
#
#     price = ADULT_PRICE if age > 18 else CHILDREN_PRICE
#
#     if current_day == "Wednesday":
#         price -= WED_DISCOUNT
#
#     print(PRINT_STATEMENT.format(price))

# value = "banana"
#
# match value:
#     case "banana":
#         print("Kela")
#     case "apple":
#         print("seb")
#     case _:
#         print("Noting")

# value = ("rectangle","circle")
#
# match value:
#     case ("rectangle"):
#         print("Only Rectangle")
#     case ("circle"):
#         print("Only Circle")
#     case("rectangle","circle"):
#         print("Rectangle and circle")
#     case _:
#         print("Noting")


value = "rectangle"

match value:
    case "rectangle":
        print("Only Rectangle")
    case "circle":
        print("Only Circle")
    case ("rectangle","circle"):
        print("Rectangle and circle")
    case _:
        print("Noting")