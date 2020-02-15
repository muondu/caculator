#Defining my function
def caculate():

    #Asks user to input
    operators = input(
    """
    Please type in the math operation you will like to complete
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """ )

    input1 = int(input("Enter your first number:  "))
    input2 = int(input("Enter your second number:  "))
    # Adding opperators
    if operators == "+":
        print(" {} + {} = " .format(input1,input2))
        print(input1 + input2)

    # Subtracting opperators
    elif operators == "-":
        print(" {} - {} = " .format(input1,input2))
        print(input1 - input2)


    # Multiplication opperators
    elif operators == "*":
        print(" {} × {} = " .format(input1,input2))
        print(input1 * input2)


    # Division opperators
    elif operators == "/":
        print(" {} ÷ {} = " .format(input1,input2)) 
        print(input1 / input2)


     #Square root  opperators
    #elif operators == "@":
        #input3 = ("Enter one number to get the square root:   ")
        #print(" √{}" .format(input3))
        #x = sqrt(input3)
        #print(x)
    else:
        print("Please put the right opperator sign")

caculate()
# Define function to ask user if they want to use the caculator again
def again():
    #Takes an input from the user
    input4 = input("""
    Do you want to use the caculator again? 
    Please type y for yes and n for no
    """)
    #Accept y in either upper or lowwer case 
    if input4.upper() ==  "Y":
        caculate()
    elif input4.upper():
         print("See you later")
    else:
        operators()
again()