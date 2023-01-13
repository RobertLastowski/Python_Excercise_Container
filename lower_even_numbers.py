number = int(input("Give me the number and I'll tell you how many smaller even numbers there are: "))
counter = 2
evens = 0
for i in range(2,number,2):
    evens += 1
    counter += 2

print(f"The number of even numbers less than {number} are {evens}")