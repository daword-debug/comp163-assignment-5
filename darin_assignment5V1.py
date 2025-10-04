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