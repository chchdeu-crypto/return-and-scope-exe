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

#mission 5
def damege_health(health,damage):
    return health-damage

def healing(hell,amou):
    return hell+amou
health_after_dam=damege_health(100,25)
finel_health=healing(health_after_dam,30)
print(finel_health)

#mission 6
def add_3_prices(num1,num2,num3):
    return num1+num2+num3
def add_discount(price,disc):
    return price-(price * (disc/100))
price_of_3_prodact=add_3_prices(50,30,20)
price_with_disc=add_discount(price_of_3_prodact,20)
print(price_with_disc)

#mission 7
def remove_space(password):
    return password.replace(" ","")
password_without_space=remove_space("2 1 44")


def print_len(password):
    return len(password)
len_password=print_len(password_without_space)

def check_len_password(password):
    if password>8:
        return True
    else:
        return False
result=check_len_password(len_password)
print(result)

#mission 8
def add_bonus(point):
    return point+5
grade_with_bonus=add_bonus(87)

def multiply(num):
    return num*1.1
grade_after_mult=multiply(grade_with_bonus)

def value_between_100(grade):
    if grade<100:
        return grade
    else:
        return 100
finel_grade=value_between_100(grade_after_mult)
print(finel_grade)

#mission 9
# def lowercase_senttence(sentence):
#     return sentence.lower()
# lower_sentence=lowercase_senttence(input("enter "))

# def count_letter_a(sentence):
#     count_a=0
#     for letter in sentence:
#         if letter == "a":
#             count_a+=1
#     return count_a
# a_in_sentence=count_letter_a(lower_sentence)

# def print_how_times_a(sentence):
#     return f"the letter a appers {a_in_sentence} times "
# result=print_how_times_a(count_letter_a)
#print(result)

#mission 10
def calculate_total_value(price,amount):
    return price*amount
toatl_value=calculate_total_value(5,5)
def calculate_total_with_storge(price):
    return price+15
storge=calculate_total_with_storge(toatl_value)
def check_price(price):
    if price>100:
        return True
    else:
        return False
    
print(check_price(storge))

#misison 11
# def return_3_letters_from_first_name(name):
#     return name[0:3]
# first_name=return_3_letters_from_first_name(input("enter name"))
# def return_3_letters_from_last_name(name):
#     return name[0:3]
# last_name=return_3_letters_from_last_name(input("enter last name"))
# def combine_names(f_name,l_name):
#     return f"{f_name}_{l_name}"
# username=combine_names(first_name,last_name)
# def lowercase_name(name):
#     return name.lower()
# finel_username=lowercase_name(username)
# print(finel_username)

#mission 12
# def calculate_fuel_per_distance(distance,fuel):
#     return distance*fuel
# total_fuel=calculate_fuel_per_distance(int(input("enter distane")),int(input("enter fuel usege")))
# def calculate_fuel_cost(total_fuel,fuel_price):
#     return total_fuel*fuel_price
# cost_fuel=calculate_fuel_cost(total_fuel,int(input("enter fuel price")))
# def divides_cost(cost,pas):
#     return cost/pas
# cost_per_passenger=divides_cost(cost_fuel,int(input("enetr how many pass")))
# print(cost_per_passenger)

#misison 13
# def get_scores_and_sum(num):
#     score_list=[int(num) for num in num.split()]
#     return sum(score_list), len(score_list)
# total_score=get_scores_and_sum(input("enter"))

# def calculate_avarge(sum_and_count):
#     total_sum=total_score[0]
#     num_scores=total_score[1]
#     return total_sum/num_scores
# avarge=calculate_avarge(total_score)
# def check_if_pass(num):
#     if num>60:
#         return "pass"
#     else:
#         return "fail"
# finel_result=check_if_pass(avarge)
# print(finel_result)

#mission 14
def return_amount(item,num):
    return f"{num} {item}"
items=return_amount("computer",4)
def adding_cost(item,price):
    amount=int(item.split()[0])
    price=amount*price
    return f"for {item} the total price is {price}"
total_price=adding_cost(items,59)
def adding_order_reday(txt):
    return f"{txt} -order ready "
order=adding_order_reday(total_price)
print(order)

#misison 15
def calculate_balance(balance,deposit):
    return balance+deposit
balance_plus_deposit=calculate_balance(100,50)
def calculate_new_balance(balance,withdrawal):
    return balance-withdrawal
balance_after_withdrawal=calculate_new_balance(balance_plus_deposit,25)
def check_if_balance_ok(balance):
    if balance>=0:
        return "ok"
    else:
        return "warning"
finel_balance=check_if_balance_ok(balance_after_withdrawal)
print(finel_balance)