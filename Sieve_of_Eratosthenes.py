print("Welcome in the Pyhton Script for Sieve of Eratosthenes, please type in the range of number in which we will search for prime numbers by typing the end of range number\n")
maximum = int(input("We will search for prime number from number 2 to...:"))
all_array = []
prime = []


for num in range(2,maximum+1):
    all_array.append(num)
print("Looking for prime numbers...")
while all_array != []:
    prime.append(all_array[0])
    all_array.remove(prime[-1])
    for item in all_array:
        if item % prime[-1] == 0:
            all_array.remove(item)

print(prime)