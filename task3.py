# Task 3: Write a function to calculate the greatest common divisor (GCD) and least common multiple (LCM) of two numbers.

# calculate gcd
def calculate_gcd(a,b):
    while b !=0:
        a,b =b , a % b
    return a

# calculate lcm
def calculate_lcm(a,b):
    return abs(a * b) // calculate_gcd(a,b)

# main function
def main():
    # input two numbers from the user
    try:
        num1=int(input("ENTER THE FIRST NUMBER: "))
        num2=int(input("ENTER THE FIRST NUMBER: "))

        # calculate gcd
        gcd=calculate_gcd(num1,num2)
        print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is: {gcd}")

        # calculate lcm
        lcm=calculate_lcm(num1,num2)
        print(f"The Least Common Multiple (LCM) of {num1} and {num2} is: {lcm}")

    except ValueError:
        print("Please enter valid integers.")

main()