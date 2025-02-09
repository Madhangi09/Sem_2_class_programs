def is_composite(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return True  # A number with divisors other than 1 and itself is composite
    return False  # If no divisors found, it's not composite

# Function to sum composite digits
def sum_composite_digits(s):
    total = 0
    for i in str(s):
        if is_composite(int(i)):  # Check if digit is composite
            total += int(i)
    return total        

# Taking input
n = int(input())
result = sum_composite_digits(n)  # Function call
print(result)
