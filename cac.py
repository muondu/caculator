import re
#Defining my function

        
def welcome():
    
    print('''
    
    welcome
    
    ''')
welcome()

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
		#checks if the opertators match with input
		if not re.match("^[+,-,*,/]*$", operators):
			print ("Error! Only characters above are allowed!")
			caculate()
			
		# checks empty space
			
		elif operators == "" :
			print('please select one of the above operators')
			caculate()

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
    elif input4.upper() == "N":
         print("See you later")
    else:
        again()

again()
