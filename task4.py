# Task 4: Implement a program to find all the prime factors of a given number

def find_prime_factors(n):
    prime_factors=[]

    while n %2==0:
        prime_factors.append(2)
        n = n //2

        # check for the odd factors from 3 ownwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i==0:
            prime_factors.append(i)
            n = n // i
    #if n is a prime number greater than 2
    if n>2:
        prime_factors.append(n)
    return prime_factors
    
number = int(input("Enter a a number to find its prime factors: "))
factors=find_prime_factors(number)
print(f"The prime factors of {number} are : {factors}")