firstNumber = input("What is the first number?")
secondNumber = input("What is the second number?")

sumOf = int(firstNumber) + int(secondNumber)
difference = int(firstNumber) - int(secondNumber)
product = int(firstNumber) * int(secondNumber)
quotient = int(firstNumber) / int(secondNumber)

print(' {} + {} = {}\n {} - {} = {}\n {} * {} = {}\n {} / {} = {}'.format(firstNumber, secondNumber, sumOf, firstNumber, secondNumber, difference, firstNumber, secondNumber, product, firstNumber, secondNumber, quotient))
