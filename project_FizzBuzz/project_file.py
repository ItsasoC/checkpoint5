def fizzbuzz_function (max_number):
    for num in range(1,max_number+1):
        if num % 3 == 0 and num %5 == 0:
            print("FizzBuzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        elif num %5 == 0:
            print("Buzz")
            continue
        print(num)

# Ejemplo:
fizzbuzz_function(20)