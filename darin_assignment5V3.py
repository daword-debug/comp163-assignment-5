print("=== Challenge 1: Collatz Conjecture ===")
n = int(input("Enter starting number:"))
step_count = 0 
print(" Sequence:",n, end=" ")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    step_count += 1

    print(n,end=" ")

print()
print("Steps:",step_count)
print()
print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input(f"Enter a number: "))
print(f"Testing divisors from 2 to {current_number - 1}")
step_count = 0

for i in range (2, (current_number-1)):
    if current_number % i == 0:
        current_number / 2
        print(f"{current_number} is not prime!")
        break
else:
    print(f"{current_number} is prime!")

print()
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("", end="")
for column in range (1,11):
    print(f"{column:4}", end="")
print()

for row in range (1,11):
    print(f"{row:2}", end=" ")
    for column in range(1,11):
        product = row * column
        print(f"{product:4}", end="")
print()
        