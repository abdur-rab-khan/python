# class Timer():
#     def __enter__(self):
#         import time
#         self.start_time = time.time()
#         print("Timer start")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         import time
#         self.end_time = self.start_time - time.time()
#         print(f"Time taken: {self.end_time} seconds")
#
# with Timer():
#     for _ in range(10000000):
#         pass

#
# file_data = open('hello.txt','r')
#
# print(file_data.readline())

with open('hello.txt') as file:
    print(file.read())