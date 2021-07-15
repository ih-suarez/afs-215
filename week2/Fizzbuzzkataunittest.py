def test_fizzbuzz():
    num = input(f'Enter a number or type done to exit: ')

    while num:
        if int(num) % 3 == 0 and int(num) % 5 == 0:
            print(f'FizzBuzz')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) == 1:
            print(f'Get {num}')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) == 2:
            print(f'Get {num}')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) == 3:
            print(f'Fizz')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) == 5: 
            print(f'Buzz')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) % 3 == 0:
            print(f'Fizz')
            num = input(f'Enter a number or type done to exit: ')
        if int(num) % 5 == 0:
            print(f'Buzz')
            num = input(f'Enter a number or type done to exit: ')
        return num

test_fizzbuzz()

