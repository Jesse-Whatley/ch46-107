varstring = "jesse"
variable = ""
varname = 2
varname = True 
print(varstring + str(varname))  
# jesse2 would be the answer using JavaScript

# if(varstring == "jesse"){} this is javascript
age = 32
if age < 30:
    print("you're young")
elif age > 30:
    print("no worrys you're still young")
else:
    print("i dont know how you get here")

#list are arrays in JS
colors = ["red", "green", "blue"]
print(colors)
colors.append("yellow")
print(colors)
colors.remove("red")
print(colors)
print(colors[2])

# for(let i = 0; i<colors.length; i++)
#   let color = colors[i];
#   console.log(color);

# for loop in python
for x in colors:
    print(x)

#dictionarys
me = {
    "first_name": "Jesse",
    "last_name": "Phillips",
    "age": 32,
}
print(me)
# get a value
print(me["first_name"]) 
# add element
me["age"]=99
me["favorit_color"]="seafoam green"
print(me)

#functions 
def say_hello():
    print("hello")

def say_goodbye(name, age):
    print("goodbye " + name + " " + str(age))

# call functions
say_hello()
say_goodbye("Jesse Phillips",32)

#creating a calculator
#functions
def print_menu():
    print("1)addition")
    print("2)subtraction")
    print("3)multiplcation")
    print("4)division")

#instructions
print_menu()
opt = int(input("Choose an option: "))
num1 = float(input("please provide the first number:"))
num2 = float(input("please provide the second number:"))

if opt == 1:
    total = num1 + num2
    print("the additions of the numbers is " + str(total))
elif opt == 2:
    total = num1 - num2
    print("the subtractions of the numbers is " + str(total))
elif opt == 3:
    total = num1 * num2
    print("the multiplications of the numbers is " + str(total))
elif opt == 4:
    if num2 == 0:
            print("you cannot divide by zero")
    else:
        total = num1 / num2
        print("the divisions of the numbers is " + str(total))