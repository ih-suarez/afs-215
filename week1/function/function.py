# Number Input
print('I will tell if a number is a Perfect Number')
num = int(input('Give me a number '))

def is_num_perfect(num):
    # Making my List of Numbers from 1 to any given number 
    # and calculating if they are divisible by the number given
    numbers_divisible = [n for n in range(1, num) if num % n == 0]

    # Adding the numbers from the list created
    numbers_total = sum(numbers_divisible)

    # If Else statement to determine whether the number given 
    # is a perfect number
    if numbers_total == num:
        print(f'Dividers of {num}: {numbers_divisible}')
        print(f'Sum of these numbers is = {numbers_total}')
        print(f'{numbers_total} = {num}')
        print(f'{num} is a Perfect Number')
    else:
        print(f'Dividers of {num}: {numbers_divisible}')
        print(f'Sum of these numbers is = {numbers_total}')
        print(f'{numbers_total} is not equal to {num}')
        print(f'{num} is not a Perfect Number')
    return num

is_num_perfect(num)