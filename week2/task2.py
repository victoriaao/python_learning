print("FizzBuzz Program")
print()

# Loop through numbers
for r in range(1, 101):
    
    # Check if number is divisible by 3 and 5
    if r % 3 == 0 and r % 5 == 0:
        print("FizzBuzz")
        
    # Check if number is divisible by 3
    elif r % 3 == 0:
        print("Fizz")
        
    # Check if number is divisible by 5
    elif r % 5 == 0:
        print("Buzz")
        
    # Otherwise, print the number
    else:
        print(r)