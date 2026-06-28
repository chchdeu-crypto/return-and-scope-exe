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
points = 3

def add_points():
    global points
    points = points + 7
    points = points * 2
    print(points)

add_points()
print(points)

