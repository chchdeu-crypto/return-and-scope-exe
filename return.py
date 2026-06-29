#mission 1
#will be printed: 8 ,10
#The 8 is printed from the function that created a new variable that only exists in the function.
#Because 10 score is outside the function and the function does not change the variable outside.

#mission 2
#will be printed: spy ,40,agent,2
#Because the variables inside the function do not affect the variables in the global.

#mission 3
#will be printed: 30 ,20
# Because we called a function with 5 inside which was increased by 10 and multiplied by 2 and the global variable was defined as 20 and did not change. 

#mission 4
# will be printed: 70 ,35,100
#Because I defined new variables inside the function and they did not affect the global variable.

#mission 5
#will be printed: map, key, torch, coin
#Because I didn't define a new variable but added it, so if it's not found in the function, it will also search globally.

#mission 6
#will be printed: potion,shield and in roe below map,key
#Because in the function I defined a new variable that does not affect the global variable.

#mission 7
#will be printed: 20 
#Because I wrote in the function that I am targeting the global variable, so it does affect it.

#mission 8
#will be printed: running, reday, wating
#Because I defined a new variable in each function that doesn't affect the function above it.

#mission 9
#will be printed: 16, 16, 10
#Because nonlocal tells it not to create a new variable but to use one that wraps me, so it changes it but not the global one.

#mission 10


#part 2
#mission 1
def converter_to_cm(meter):
    return meter*100
cm=converter_to_cm(5)

def how_far(move):
    return f"robot moved {move} cm"
robot_moved=how_far(cm)
print(robot_moved)

#mission 2
def add_price_delivery(price):
    return price+10
def multy_price(price):
    return price*2
price_with_del=add_price_delivery(340)
finel_price=multy_price(price_with_del)
print(finel_price)

#mission 3
def return_full_name(first_name,last_name):
    return first_name+ last_name
def upper(name):
    return name.upper()
full_name=return_full_name("chaim","deusth")
user_name=upper(full_name)
print(user_name)

#mission 4
def cel_to_fah(cell):
    return cell*9/5+32
def sentence(mess):
    return f"the temperature is: {mess}"
fha=cel_to_fah(38)
temperature=sentence(fha)
print(temperature)


