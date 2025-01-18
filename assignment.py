def format_string(name, age):
      return f" My name is {name} and I am {age} years old"

name = input("Enter your name : ")
age  = int(input("Enter your age "))
print(format_string(name, age))

def conditional_check(number):
     
     if number == 10:
        print("Number is EQUAL to 10")
     elif number > 10:
        print("number is GREATER than 10")
     else:
        print("Number is LESS than 10")

number = int(input("Enter your number"))
print(conditional_check(number))   

def loop_sum(n):
    sum = 0
    for num in range (1, n+1):
        sum = sum + num
    print("The sum is :" ,sum)

n =int(input("Enter uper limit: "))
print(loop_sum(n))

def list_operations(numbers):
    largest = numbers[0]
    sum=0
    min = numbers[0]

    for num in numbers:
        sum = sum + num
    print(" the sum is : " ,sum)

    for num in numbers:
        if num > largest:
            largest = number
    print("the maximu is : ",largest)

    for num1 in numbers:
        if num1 < min:
            min = num1
    print("the minimun is : ",min)

numbers =[35,23,11,45,10,9,53]
print(list_operations(numbers))

def dict_operations(students_dict):
    std_names = []

    for names, scores in students_dict.items:
        if scores > 80:
            std_names.append(names)
        print(std_names)
        

students_dict ={
       "Juma" :79,
       "Asha" : 82,
       "Leo" :94,
       "James":85,
       "Emmy": 80,
       "Abu":56,
       "Happy":68

   } 

list1 = [1, 2, 63, 44, 25]
list2 = [4, 25, 63, 7, 8]
def set_operations(list1, list2):
    set1 = set(list1)  # Convert list1 to a set
    set2 = set(list2)  # Convert list2 to a set
    
    # Find common elements using the intersection method
    common_elements = set1.intersection(set2)
    
    return common_elements
print(set_operations(list1,list2))

def arithmetic_ops(a, b):
    answer ={}

    answer["sum"] = a+b
    answer["difference"] = a-b
    answer["product"] = a*b
    if b != 0:
        answer['quotient'] = a / b
    else:
        answer['quotient'] = 'undefined'  # Return 'undefined' if division by zero
    
    return answer

a = 10
b = 5
answer = arithmetic_ops(a, b)
print(answer)  

def logical_ops(x, y):
    result = {}
    result['and'] = x and y
    result['or'] = x or y
    result['not_x'] = not x
    
    return result

x = True
y = False
result = logical_ops(x, y)
print(result)

def bitwise_ops(a, b):
    opp = {}
    
    opp['and'] = a & b
    
    opp['or'] = a | b
    
    opp['xor'] = a ^ b

    return opp
a= 8
b =13
opp = bitwise_ops(a, b)
print(opp) 