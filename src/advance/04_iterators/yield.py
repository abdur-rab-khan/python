# def read_file(filename):
#     with open(filename, "r") as file:
#         lines = file.readlines()  # Reads the entire file into memory
#     return lines
#
# # Process the file
# lines = read_file("example.txt")
# error_count = 0
# for line in lines:
#     if "error" in line:
#         error_count += 1
#
# print("Total errors:", error_count)

#
# def simple_generator():
#     yield "apple"
#     yield "banana"
#     yield "cherry"
#
# gen = simple_generator()
#
# # First way to get the generator values
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
#
# # Second way to get the generator values
#
# for val in simple_generator():
#     print(val)


# def read_file_lazily(filename):
#     with open(filename, "r") as file:
#         for line in file:  # Reads one line at a time
#             yield line  # Yields the line to the caller
#
# # Process the file
# error_count = 0
# for line in read_file_lazily("example.txt"):
#     if "error" in line:
#         error_count += 1