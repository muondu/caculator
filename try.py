import re

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
			
caculate()