greetings = "Welcome !"

def greet():
    # Greetings is the global variable, this is why i can access it inside the function.
    print(greetings)
    
greet()

# As greetings is a global variable, it can work outside a function.
print(greetings)

def name():
    last_name = "Jeremy"
    print(last_name)
    
name()
# As last_name is a local variable of the function name it can work inside it however outside it cant be used out of the function.
# print(last_name)

def name2():
    global first_name 
    first_name = "William"
    print(first_name)
    
name2()

# the reason why we can print the first_name variable outside of the function this time is due to the fact we made it a global variable prior to the print within the function in which it originated from.
print(first_name)

def sum(num1, num2):
    return num1 + num2

result = sum(5, 7)
print(result)

sum1 = lambda num1, num2: num1+num2

result2 = sum1(4,2)

print(result2)

# the lambda function to multiply two numbers

sum2 = sum(6,4)

multiply = lambda num1, num2: num1*num2

result3 = multiply(66,974)

print(result3)

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

# Write the code to find the remainder of the number when divided by 4

remainders = list(map(lambda num: num % 4, number))

print(remainders)

def kmh2mps(speed):
    vehichle = "car"
    global new_speed
    new_speed = speed*5/18
    return new_speed

result5 = kmh2mps(66)

print(result5)