# Task 1: Write a program to check if a number is prime, and also list all prime numbers up to that number.
def is_prime(n):
# check if the number is prime
    if n<=1:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
        else:
            return True
    
def list_prime(n):
# list all prime numbers up to a given number
    prime  =[]
    for num in range(2,n+1):
        if is_prime(num):
            prime.append(num)
    return prime

# main function
def main():
    # input the number from the user
    num= int(input("ENTER A NUMBER: "))
    # check if the number is prime.
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

    # list all prime numbers up to the given number
    prime =list_prime(num)
    print(f"Prime numbers up to {num}: {prime}") 

main()