def sum_list(numbers):
    result = sum(numbers)
    return f'The sum of {numbers} is {result}'

numbers = []

num_of_elements = int(input("Enter the number of elements you want to add to the list: "))

for i in range(num_of_elements):
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)

print(sum_list(numbers))
