def test_fizzbuzz():
    test_testing = True

    while test_testing:
        num = input(f'Enter a number: ')
        if int(num) % 3 == 0 and int(num) % 5 == 0:
            print(f'FizzBuzz')
            continue
        if int(num) == 1:
            print(f'Get {num}')
            continue
        if int(num) == 2:
            print(f'Get {num}')
            continue
        if int(num) == 3:
            print(f'Fizz')
            continue
        if int(num) == 5: 
            print(f'Buzz')
            continue
        if int(num) % 3 == 0:
            print(f'Fizz')
            continue
        if int(num) % 5 == 0:
            print(f'Buzz')
            continue
        else:
            test_testing = False
            print(f'Test Failed: Invalid Input.')
            print(f'test_testing = {test_testing}')
            break
test_fizzbuzz()

