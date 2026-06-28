#mission 1
#will be printed: 8 ,10
#The 8 is printed from the function that created a new variable that only exists in the function.
#Because 10 score is outside the function and the function does not change the variable outside.

#mission 2

name = "Agent"
level = 2

def show_info():
    name = "Spy"
    level = 4
    power = level * 10
    print(name)
    print(power)

show_info()
print(name)
print(level)

