#1
def square(num):
    return num **2
print(square(4))

#2
def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4]))

#3
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

#4
def is_prime (num1):
    if num1 <= 1:
        return False
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i== 0:
            return False
    return True
print (is_prime(7))
print(is_prime(10))