def add(num1, num2):
    return num1 + num2

print("Please select operation -\n" \
        "1. Add\n" )

select = int(input("Select operations form 1:"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  