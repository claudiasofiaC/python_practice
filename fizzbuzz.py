#a = 1,2,3,4,5,6,7,8,15

def fizz_buzz(int):
    if (int % 3 == 0) and (int % 5 == 0):
        return "FizzBuzz"
    if int % 3 == 0:
        return "Fizz"
    if int % 5 == 0:
        return "Buzz"

    return input

#print(fizz_buzz(100))
