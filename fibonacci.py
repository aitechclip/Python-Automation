def generate_fibonacci(n):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibonacci_numbers = generate_fibonacci(n)
    print("Generated Fibonacci numbers:", fibonacci_numbers)
