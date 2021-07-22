def test_fizzbuzz(num):
    if int(num) % 3 == 0 and int(num) % 5 == 0:
        return f'FizzBuzz'
        
    if int(num) == 1:
        return f'Get {num}'
        
    if int(num) == 2:
        return f'Get {num}'
        
    if int(num) == 3:
        return f'Fizz'
        
    if int(num) == 5: 
        return f'Buzz'
        
    if int(num) % 3 == 0:
        return f'Fizz'
        
    if int(num) % 5 == 0:
        return f'Buzz'
    return num


if __name__ == '__main__':
    for i in range(1, 101):
        print(test_fizzbuzz(i))