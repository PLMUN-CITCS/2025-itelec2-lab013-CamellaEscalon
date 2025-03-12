# Create a list of numbers from 1 to 10 using range and list functions
numbers = list(range(1, 11))

# Iterate over each number in the numbers list
for num in numbers:
    # If the number is 3, skip the rest of the loop iteration
    if num == 3:
        continue  # Skip the rest of this iteration
    
    # If the number is 7, exit the loop completely
    if num == 7:
        break  # Exit the loop completely
    
    # Print the current number
    print(num)
