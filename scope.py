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