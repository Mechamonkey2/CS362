def hello_world():
    return 'Hello World!'

def FizzBuzz(num):
    if not num % 15:
        return("fizzbuzz")

    if not num % 3:
        return("fizz")

    if not num % 5:
        return("buzz")

    return num

def print100():
    for num in range(1,11):
        while(num<=100):
            print(num," ", end ="")
            num+=10
        print()
