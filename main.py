# Let's choose two prime numbers, p = 7 and q = 11.
#     n = p * q = 7 * 11 = 77.
#     Compute the Euler's totient function: φ(n) = (p - 1) * (q - 1) = 6 * 10 = 60.
#     Choose a public exponent, e. Let's use e = 13, which is coprime to 60.

num_1 = int(input("Enter a prime number : "))
num_2 = int(input("Enter a prime number : "))

# # finding "n"

n = num_1 * num_2

# # finding Euler's Totient :- 

et_n = (num_1 - 1) * (num_2 - 1)

temp = et_n

# finding the prime numbers 
my_list = []

n = 0
i = 0
while n<100:
    i+=1
    count = 1
    for j in range(2,i):
        if i%j==0:
            count=0
            break
    
    if count == 1:
        my_list.append(i)
        n+=1

# print(my_list)

for list_temp in my_list:
    if temp == num_1 or temp == num_2:
        print(f"{list_temp} is already taken.")

    elif(temp % list_temp == 0):
        factor = list_temp
        print(f"{list_temp} is a factor of {temp}.")
        my_list.remove(list_temp)


print(my_list,end=' ')

