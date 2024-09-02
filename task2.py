# Task 2: Create a program that generates the first 30 Fibonacci numbers using both iterative and recursive approaches.

# firstly,generate the first n fibonnaci numbers using an iterative approach 

def fibonnaci_iterative(n):
    fib_sequence = [0,1]
    for i in range(2,n):
# add the sum of the last two numbers in the sequence
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
        # return the first n fibonnaci numbers
    return fib_sequence[:n]   

# secondly,generate the nth fibonnaci number using a recursive approach
def fibonnaci_recursive(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci_recursive(n-1)+fibonnaci_recursive(n-2)

def generate_fibonnaci_recusive(n):
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(fibonnaci_recursive(i))
    return fib_sequence

# main function
def main():
    n=int(input("enter the number: "))

    print("Fibonnaci sequence using iterative approach: ")
    fib_iterative =fibonnaci_iterative(n)
    print(fib_iterative)

    print("\nFibonnaci sequence using recursive approach: ")
    fib_recursive = generate_fibonnaci_recusive(n)
    print(fib_recursive)

main()