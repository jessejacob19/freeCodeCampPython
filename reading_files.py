'''
different modes to open a file
r - read - only read
w - write - change file
a- append - append stuff on to the end of the file
r+ - read and write
'''

employee_file = open("employees.txt", "r")
#print(employee_file.readable())
#print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
print(employee_file.readlines()) # each line is in an array


employee_file.close()


employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")


employee_file.close()

employee_file = open("employees.txt", "w")

employee_file.write("\nKelly - Customer Service")