# print a count of a seconds.

count = 1
count_end = 60
while (count <= count_end):
    print("The count is",count)
    count += 1
count -= 1
print("Count completed", count,"times")


count = 1
count_end = int(input("Enter ending count:"))

while (count <= count_end):
    print("The count is",count)
    count += 1
count -= 1
print("Count completed", count,"times")
